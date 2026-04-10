# Designing Data Intensive Applications - Martin Kleppmann, Chris Riccomini

> There are no solutions. There are only trade-offs ~Thomas Sowell

## 1. Trade-Offs in Data Systems Architecture

**Compute Intensive** - parallelizing - challenge
**Data Intensive** - concurrency, consistency - challenge

databases, caches, search indexing, stream processing, batch processing. 

### Operational Vs Analytical Systems

Backend Engineers 
Business Analysts, Data Scientists

Data Engineers - Connect Operational, Analytical
Analytical Engineers - Model, Transform

**Point Query** lookup records by key. 

**OLTP** Online Transaction Processing
**OLAP** Online Analytical Processing
**HTAP** Hybrid Transactional/Analytical Processing
**Product Analytics / Real Time Analytics** -- embedded into user-facing products

**Data Warehouse** database for analytics. aggregations. relational data model
**Data Lake** centralized data repository. avro, parquet. cheaper commoditized file storage. object stores. 

**ETL** Extract, Transform, Load
**ELT** Extract, Load, Transform

Tableau, Looker, or Microsoft Power BI - **Data Visualization / Dashboard**
Pinot, Druid, and ClickHouse - **Product Analytics**
Fivetran, Singer, or Airbyte - **ETL for API**
Spark - **Distributed Anlytics**
TFX, Kubeflow, or MLflow - **ML Deployment Tools**
MySQL, PostgreSQL, MongoDB - AWS Aurora, Azure SQL DB Hyperscale, Google Cloud Spanner - **OLTP**
Teradata, ClickHouse, Spark - Snowflake, Google BigQuery, Azure Synapse Analytics - **OLAP**
OpenTelemetry, Zipkin, and Jaeger - **Tracing tools** Which client called which tool how much time did it take
DuckDB, SQLite, and KùzuDB - **Single Node Databases**
OpenAPI, gRPC - **API Description Standards** manage relationship between client and server APIs
HdrHistogram, t-digest, OpenHistogram, and DDSketch - **Open Source Percentile Estimation Libraries**

**Data Pipelines** ETL Processes. Data Integration. 
Operational Systesm -> Data Lake -> Data Warehouse 

**Sushi Principle** Raw data is better. 

**GDPR** General Data Protection Regulation
**CCPA** California Consumer Privacy Act

**Reverse ETL** Output of analytical systems is made available to Operational Systems. 

**Systems of Record** Source of Truth
**Derived Data Systems**


<br/><br/>



### Cloud Vs Self Hosting 

Software - who builds, who deploys? How they deploy?

In-house software, in-house operations; 
Off-the-shelf software, in-house operations;
Off-the-shelf software, outsourced operations;

Open source, commercial. 

Kubernetes orchestration framework. 

Cloud Services. Subscribing instead of buying. Renting. 

**Cloud Native Architecture** designed to take advantage of cloud services. 

**RDMA** Remote Direct Memory Access
**RAID** Redundant Array of Independent Disks - tolerate failure of individual disk. 

**Virtual Disk** - every IO is a network call. Emulates disk behavior. 

**Storate and Compute Separation**. To analyze data, data must first be transferred over network. 

**Multitenant** - shared hardware

**DBA** Database Administrators. sysadmins. 
**DevOps** Software Development + Operations
**SRE** Site Reliability Engineer. Google's implementation of DevOps

Operations - configure, deploy, monitor, diagnose. goal is to provide reliable service. 
Metered Billing removes need for capacity planning -> Financial Planning. 
Performance Optimization -> Cost optimization. 


<br/><br/>


### Distributed vs Single-Node Systems

**Distributed System** systems communicate over network. 
Each is called a **Node**

**Observability** techniques for diagnosing distributed systems. collects execution data. 

**SOA** Service Oriented Architecture; Clients, Servers, communicating over network. HTTP. 
Microservices architecture, **service** has one well-defined purpose. Exposes API clients can use. Each service usually has its own Database. 

**Microservice** technical solution to a people problem. Allows teams to make progress independently. 

**Serverless** - **FaaS** Function as a Service. 

**HPC** High Performance Computing. Supercomputing. 


<br/><br/>


### Data Systems, Law, Society

**Data Minimization** some data is simply not worth storing. Safety risks for users. Ex: when governments force to hand over data. 

**PCI** Payment Card Industry
**SOC** Service Organizational Control - Vendors



<br/><br/>


<br/><br/>

## 2. Defining Non Functional Requirements

Performance, Reliability, Scalability, Maintainability

**Polling** running query at an interval
**Fan out** deliver posts to each follower. One initial request results in several downstream requests. 

**Materialization** precomputing and updating the results of a query - view. Faster reads, more work on writes. 

**Response Time** from request to response - what user sees including delays
**Service Time** duration for which service processes clients request
**Throughput** number of requests per second
**Queueing Delays** waiting for CPU or packet to be buffered before sending over network
**Latency** time during which request is not actively processed. network latency or delays


**Metastable Failure** - Retry Storm. Long waiting queue of requests, maximum throughput, increased response times, time out, retries. Even after load is reduced, system might be in overloaded state until rebooted. 

**Exponential Backoff** increase and randomize time between successful retries
**Circuit Breaker or Token Bucket Algorithm** temporarily stop sending requests to a service that returned errors or timed out 
**Load Shedding** proactively reject requests when approaching overload
**Backpressure** send back responses asking clients to slow down
**Head-of-line blocking** slow requests holding up processing of subsequent requests

**Scalable** maximum throughput can be significantly increased by adding compute
**Jitter** variation in network delay

Mean is not typical
Median is **50th Percentile**
**Tail Latencies** High Response Time Percentiles
**Tail Latency Amplification** even if a small percentage of backend calls are slow, the chance of getting slow call increases if end-user request requires multiple backend calls. just a single slow call can slow down the entire end-user request. The probability of hitting a slow "tail" increases exponentially with the number of parallel calls.


**SLO** Service Level Objectives - sets target for a service
**SLA** Service Level Agreements - contract specifies what happens if target is not met. 

**Fault** when a particulate part of the system stops working correctly. Hardware faults. Software faults.
**Failure** system as a whole stops providing service. does not meet SLO. 
**Fault-Tolerant** system continues providing services inspite of certain faults. 
**SPOF** Single Point of Failure - system can not tolerate certain part becoming faulty. 
**Fault Injection** deliberately inducing faults. randomly killing processes without warning. 

**Exactly-once semantics** without missing any posts that should have been delivered and without creating duplicates. Social Media Fan Out Case Study. 
**Chaos Engineering** aims to improve confidence in fault-tolerance through experimentation. 

**ECC** Error Correcting Codes. 

**Redundancy** most effective when faults or independent. not correlated. Cloud focus less on individual machines. Aim to make services available by tolerating faulty nodes at software level. 

**Availability Zones** identify which resources are physically co-located. 

**Rolling Upgrade** multi-node fault-tolerant system can be patched by restarting one node at a time without affecting service for users. 

> Do not assume that the software works correctly all the time. 

Scalability investments are **wasted effort** and **premature optimization**.

Understand load. read write ration, cache hit rate, ...

**Vertical Scaling / Scaling Up** upgrading machine. 
**Shared memory architecture** threads of same process can access memory
**Shared disk architecture** systems sharing the disk and connected by fast network
**NAS** Network Attached Storage
**SAN** Storage Area Network
**Shared Nothing Architecture** aka **Horizontal Scaling / Scaling Out** involves distributed system

**Operable** smooth running of system
**Simplicity** easy to understand
**Evolvability** easy to make changes

**Big ball of mud** software project mired in complexity

**essential complexity** (inherint in problem tooling)
**accidental complexity** limitations of our tooling

**Design Patterns**
**DDD Domain Driven Design**
**Abstraction** can help manage complexity. 

**Agile** adpat to change
**TDD Test Driven Development**
**Evolvability** Agility on Data System Level


<br/><br/>


<br/><br/>


## 3. Data Models and Query Languages


## 4. Storage and Retrieval

## 5. Encoding and Evolution

## 6. Replication

## 7. Sharding

## 8. Transactions

## 9. The truble with distributed systems

## 10. Consistency and Consensus

## 11. Batch processing

## 12. Stream processing

## 13. Philosophy of streaming systems

## 14. Doing the right thing
