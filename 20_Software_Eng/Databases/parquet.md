### 📝 Cheat Sheet: Columnar Storage & Blocks
*Initial Query: what is columnar storage; what are blocks; how is information stored;*

#### 🧠 Core Concepts
* **Columnar Storage**: Data is stored physically by **column** instead of by row. Contiguous storage of identical data types.
* **Blocks / Micro-partitions**: Immutable physical storage chunks on disk/cloud. Each block holds data for specific columns.
* **Storage Mechanism**: 
    1. Isolate columns.
    2. Apply <span style="color: #007acc;">**aggressive compression**</span> (RLE, Dictionary).
    3. Write to immutable blocks.
    4. Store **metadata** (min/max) centrally for partition pruning.

#### 🏗️ Real-World Application
* **OLAP / Data Warehousing**: The standard for Snowflake, BigQuery, Redshift.
* **I/O Efficiency**: `SELECT SUM(Amount)` reads *only* the 'Amount' block. Skips all unqueried columns, saving massive I/O.

#### ⚠️ Caveats & Gotchas (The "Do Nots")
* *Avoid* **OLTP Workloads**: Highly inefficient for rapid, single-row `INSERT`, `UPDATE`, or `DELETE` operations (requires rewriting multiple blocks).
* *Avoid* `SELECT *`: Incurs heavy CPU penalty for **Tuple Reconstruction** (stitching columns back into rows).
* *Immutability*: Updates cause fragmentation (tombstoning); requires background compaction/clustering.


<br/><br/>

Apache Parquet
Columnar storage
open source
