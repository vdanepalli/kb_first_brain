dimensional modeling
measurements and context
facts and dimensions


relational database - star schema
multidimensional database - cube

operational systems - business process execution
transactions
oltp
third normal form
insert, update, delete
acid
er model
concurrency

analytics systems - evaluation of business process
aggregations
performance
star schema, cube
data mart
data warehouse
dimensional design


without context, measurement is useless
measurements = facts -- usually numeric, rollup or breakout
context = dimensions -- by, for -- filters, query predicates -- groupings, break levels

snowflake
outriggers
surrogate key for each dimension table - warehouse keys - primary key of dimension table
natural keys


slowly changing dimensions -- scds. 
fact tables grain -- level of detail


corporate information factory - inmon
operational systems -> ETL -> enterprise data warehouse - relational; 3NF
enterprise data warehouse -> data marts (dimensional) -- data delivery


bus architecture
dimensional data warehosue - kimball architecture


stand alone data marts - islands of information
stovepipes


type 2 slow change
multi column foreign key

