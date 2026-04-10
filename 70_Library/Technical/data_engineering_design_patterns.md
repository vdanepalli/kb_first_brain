# Data Engineering Design Patterns ~ Bartosz Konieczny

## 1. Introducing Data Engineering Design Patterns

**Dead lettering** handling erroneous records without breaking the pipeline

**Singleton Pattern** to avoid allocating unnecessary objects

**Medallion architecture** dataset may live in one of three different layers: Bronze, Silver, and Gold

Bronze - **raw**; Silver - **cleansed, enriched**; Gold - **exposes to final users**

**23 Software Engineering Design Patterns** Gang of Four design patterns (4 authors)

**backfiling** processing past data. subtly different from **reprocessing** (usually reprocessing indicates data was already processed before but had issues or something changed)

1. Data Ingestion
2. Data Replication
3. Data Readiness


## 2. Data Ingestion Design Patterns

### **1. Pattern: Full Loader** 

data ingestion scenario that works on a complete dataset each time

Implementation 1: **Extract and Load** aka **Passthrough Jobs**

**Transactions** automatically manage data visibility, and they’re the easiest mitigation of this **concurrency** issue.

**single data exposition abstraction** if transactions are not supported. 

**time travel** feature, such as Delta Lake, Apache Iceberg, or Google Cloud Platform (GCP) BigQuery


```bash
# Sync Buckets
aws s3 sync s3://input-bucket s3://output-bucket --delete

# Loading data to versioned table
COPY devices_${version} FROM '/data_to_load/dataset.csv' CSV  DELIMITER ';' HEADER;

# Exposing one versioned table publicly
CREATE OR REPLACE VIEW devices AS SELECT * FROM devices_${version}
```

```py
# Extract load implementation with Apache Spark and Delta Lake
input_data = spark.read.schema(input_data_schema).json("s3://devices/list")

input_data.write.format("delta").save("s3://master/devices")
```

<br/><br/>


### **2. Pattern: Incremental Loader**

Implementation 1 uses **delta column** to identify rows added since the last run.
Implementation 2 uses **time partitioned datasets**

**Readiness Marker pattern.**

**data producer** emits late data (see **“Late Data”**) for the event time you already processed. So using event timestamp is risky. 

delta column implementation needs to remember the **last ingestion time** value to incrementally process new rows.

When a data provider deletes a row, the information physically disappears from the input dataset. However, it’s still present in your version of the dataset because the delta column doesn’t exist for a deleted row. To overcome this issue you can rely on **soft deletes**, where the producer, instead of physically removing the data, simply marks it as removed. Put differently, it uses the **UPDATE operation instead of DELETE.**

The **insert-only** tables are also known as **append-only** tables.

`delta_column BETWEEN ingestion_time AND ingestion_time + INTERVAL '1 HOUR'`


```bash
# Sync S3 Buckets
aws s3 sync s3://input/date=2024-01-01 s3://output/date=2024-01-01 --delete


```

**File​Sensor** check if next partition is available. AwsGlue​Catalog​Partition​Sensor, Big​Query​Table​PartitionExistenceSensor, or DatabricksPartitionSensor

```py
# Incremental Loader DAG example
next_partition_sensor = FileSensor(
 task_id='input_partition_sensor',
 filepath=get_data_location_base_dir() + '/{{ data_interval_end | ds }}',
 mode='reschedule',
)
load_job_trigger = SparkKubernetesOperator(application_file='load_job_spec.yaml',
 # ... omitted for brevity
)
load_job_sensor = SparkKubernetesSensor(
 # ... omitted for brevity
)

next_partition_sensor >> load_job_trigger >> load_job_sensor
```

```js
// Incremental Loader DAG example
next_partition_sensor = FileSensor(
 task_id='input_partition_sensor',
 filepath=get_data_location_base_dir() + '/{{ data_interval_end | ds }}',
 mode='reschedule',
)
load_job_trigger = SparkKubernetesOperator(application_file='load_job_spec.yaml',
 # ... omitted for brevity
)
load_job_sensor = SparkKubernetesSensor(
 # ... omitted for brevity
)

next_partition_sensor >> load_job_trigger >> load_job_sensor
```

```py
# Incremental Loader for transactional (not partitioned) dataset
load_job_trigger = SparkKubernetesOperator(
  # ...
  application_file='load_job_spec_for_delta_column.yaml',
)
load_job_sensor = SparkKubernetesSensor(
  # ...
)

load_job_trigger >> load_job_sensor
```

```py
# Data ingestion job with delta column and time boundaries
in_data = (spark_session.read.text(input_path).select('value',
   functions.from_json(functions.col('value'), 'ingestion_time TIMESTAMP')))
    
input_to_write = in_data.filter(
  f'ingestion_time BETWEEN "{date_from}" AND "{date_to}"'
)

input_to_write.mode('append').select('value').write.text(output_path)
```

<br/><br/>


### **3. Pattern: Change Data Capture**

The pattern consists of **continuously ingesting** all modified rows directly from the internal database **commit log**. 

A **commit log** is an **append-only** structure.

CDC will bring **additional metadata** with the records, such as the operation type (update, insert, delete), modification time, or column type. 

the pattern **ingests data at rest**. As a side effect, these static rows become **data in motion**

Commit log reader: **Debezium (open source)** 
**Debezium implementations**: **Kafka Connect** (act as bridge between rest and moving data), Debezium Embedded Engine and Debezium Server.

```json
# Debezium Kafka Connect configuration for PostgreSQL
{
  "name": "visits-connector",
  "config": {
    "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
    "database.hostname": "postgres", "database.port": "5432",
    "database.user": "postgres", "database.password": "postgres",
    "database.dbname" : "postgres", "database.server.name": "dbserver1",
    "schema.include.list": "dedp_schema",
    "topic.prefix": "dedp"
  }
}
```

**lake-native** formats do support CDC in a simpler way

**Delta Lake** has a **built-in change data feed (CDF)** feature to stream the changed rows that you can enable either as a global session property or as a local table property with the `readChangeFeed` option.

```py
# CDF setup in Delta Lake
spark_session_builder
  .config('spark.databricks.delta.properties.defaults.enableChangeDataFeed', 'true')

spark_session.sql('''
  CREATE TABLE events (
    visit_id STRING, event_time TIMESTAMP, user_id STRING, page STRING
  )
  TBLPROPERTIES (delta.enableChangeDataFeed = true)''')

# CDF usage in Delta Lake
events = (spark_session.readStream.format('delta')
 .option('maxFilesPerTrigger', 4).option('readChangeFeed', 'true')
 .option('startingVersion', 0).table('events'))
query = events.writeStream.format('console').start()
```


<br/><br/>

**Replication** is about moving data between the **same type of storage** and ideally preserving all its metadata attributes

**Loading** is more flexible and doesn’t have this homogeneous environment constraint.


<br/><br/>

### **4. Pattern: Passthrough Replicator**

**Not Idempotent**: it may return different results for the same API call

Solution can be at **compute** level or **infrastructure** level. 

**compute** implementation relies on the **EL job**

**infrastructure** part is based on a **replication policy** document where you configure the input and output location and let your **data storage provider replicate** the records on your behalf.

simplest: **data copy command** available in the database 

you should implement the replication with the **push** approach **instead of pull.**

**environment owning** the dataset **will copy** it to the others

For **Apache Kafka topic replication**, you could use the **MirrorMaker utility**



```py
# JSON data replication with Apache Spark
input_dataset = spark_session.read.text(f'{base_dir}/input/date=2023-11-01')
input_dataset.write.mode('overwrite').text(f'{base_dir}/output-raw/date=2023-11-01')
```

```py
# Passthrough Replicator with an ordering semantic
events_to_replicate = (input_data_stream
  .selectExpr('key', 'value', 'partition', 'headers', 'offset'))

def write_sorted_events(events: DataFrame, batch_number: int):
  (events.sortWithinPartitions('offset', ascending=True).drop('offset').write
  .format('kafka').option('kafka.bootstrap.servers', 'localhost:9094')
   .option('topic', 'events-replicated').option('includeHeaders', 'true').save())

write_data_stream = (events_to_replicate.writeStream
   .option('checkpointLocation', f'{get_base_dir()}/checkpoint-kafka-replicator')
   .foreachBatch(write_sorted_events))
```

```python
# AWS S3 bucket replication
resource "aws_s3_bucket_replication_configuration" "replication" {
  role   = aws_iam_role.replication.arn
  bucket = aws_s3_bucket.devices_production.id

  rule {
    id = "devices"
    status = "Enabled"
    destination {
      bucket        = aws_s3_bucket.devices_staging.arn
      storage_class = "STANDARD"
    }
  }
}
```


<br/><br/>


### 5. Pattern: Transformation Replicator

**Anonymizer pattern** replicating attributes that should not be replicated

source and target schema datetimes use different format. instead of defining the timestamp columns as is, you can simply **configure them as strings** **to avoid any silent transformations.**

Implementation 1: **Data reduction** eliminate unncessary fields

Fine-Grained Accessor Pattern

```sql
-- Dataset reduction with EXCEPT operator
SELECT * EXCEPT (ip, latitude, longitude)

-- Column-level access for user_a on table visits
GRANT SELECT (visit_id, event_time, user_id) ON TABLE visits TO user_a  
```

```py
# Dataset reduction with drop function
input_delta_dataset = spark_session.read.format('delta').load(users_table_path)
users_no_pii = input_delta_dataset.drop('ip', 'latitude', 'longitude')
```

Implementation 2: **column-based transformation** to alter the sensitive fields

```py
devices_trunc_full_name = (input_delta_dataset
  .withColumn('full_name', 
      functions.expr('SUBSTRING(full_name, 2, LENGTH(full_name))'))
)
```

```scala
case class Device(`type`: String, full_name: String, version: String) {
  lazy val transformed = {
    if (version.startsWith("1.")) {
      this.copy(full_name = full_name.substring(1), version = "invalid")
     } else {
        this
     }
  }
}
inputDataset.as[Device].map(device => device.transformed)
```

<br/><br/>


### 6. Pattern: Compactor

Having **small files** is a well-known problem. Longer listing operations and heavier I/O for opening and closing files.

**Compactor pattern** addresses the problem by **combining multiple smaller files** into bigger ones, thus reducing the overall I/O overhead on reading.

**Open Table Formats**

**Apache Iceberg** performs this via a `rewrite` data file action, while **Delta Lake** employs the `OPTIMIZE` command.

`Apache Hudi`, which is the third open table file format. A **Hudi table** can be configured as a **merge-on-read (MoR)** table where the **dataset is written in columnar format** and any **subsequent changes are written in row format.** **Compaction** operation then **merges** changes from **row storage with columnar storage**

**Compactor** also works for non-lake-related storage. **Apache Kafka**, which is an **append-only key-based logs system**


Compaction is much simpler and safer to implement in modern, **open table file formats** with **ACID properties** (such as Delta Lake and Apache Iceberg) than in raw file formats (such as JSON and CSV).

To delete source small files **`VACUUM`**, which are available in modern data storage technologies like Delta Lake, Apache Iceberg, PostgreSQL, and Redshift.


```py
# Compaction job with Delta Lake
devices_table = DeltaTable.forPath(spark_session, table_dir)
devices_table.optimize().executeCompaction()

# VACUUM in Delta Lake
devices_table = DeltaTable.forPath(spark_session, table_dir)
devices_table.vacuum()
```

Unlike in the Delta Lake example, **Kafka’s** compaction is **nondeterministic.** You can’t expect it to run on a regular schedule, and as a result, it doesn’t guarantee that you’ll always see a unique record for each key.



<br/><br/>

### 7. Pattern: Readiness Marker



<br/><br/>

### 8. Pattern: External Trigger
