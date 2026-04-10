# Learning Snowflake SQL and Scripting ~Alan Beaulieu

## Foundations 1: Chapter 1-5 

Chapters: Querying; Filtering; Joins; Sets; Creating and Modifying data

**Primary Key**
**Foreign Key**
**Normalization** making sure each independent piece of information is in only one place except for foreign keys. 

**Snowflake** first launched **2014**;  **SaaS**

**DDL Data Definition Language** Create table, create index, alter table
**DML Data Manipulation Language** Select, Insert, Update, Delete, Merge
**Transactions** Commit, Rollback

**SQL** is **Nonprocedural** language. You define what you want done, not how to do it. 

**PL/SQL** Oracle procedural language. 
**Transact SQL** Microsoft procedural language. 

```sql
create or replace database learning_sql;
use schema learning_sql.public;
create table region as select * from snowflake_sample_data.tpch_sf1.region;
```

**Snowsight**
**SnowSQL**

```bash
!set prompt_format=[schema]>;
```

```sql
show tables;
describe table region;
```

select; 
from;
where;
group by;
having; 
qualify; -- filters results of windowing functions. 
order by; 
limit; 



<br/><br/>

literals
expressions
built-in function calls
user-defined function calls


<br/><br/>

column aliases. 
select distinct - server sorts values, and removes duplicates. 

```sql
select * from values
    ('JAN', 1),
    ... 
    ('DEC', 12)
as months(month_name, month_number);
```

```sql
select 
    n_name, 
    rank() over (order by length(n_name) desc) as length_rank 
from nation
qualify length_rank <= 5;
```

```sql
select s_name, s_acctbal from supplier
order by s_acctbal desc
limit 10 offset 7390; -- skip first 7390, and then fetch 10. 
```

```sql
select top 10 s_name, s_acctbal from supplier
order by s_acctbal desc; -- top does not support offset. 
```

Comparision operators: <, >, =, <>, !=, between, in, not in, like, is null, is not null

`regexp_like(col, pattern, parameters)`

`.*`  anything. same as `%`
`[0-9]` any single number
`[a-zA-Z]` 
`^` start of the string
`$` end of the string
`{n}` exactly n times. 
`+` one or more
`*` zero or more
`.` any single character. 
`\d` any singe digit

`REGEXP_LIKE(zip_code, $$\d{5}$$` wrapping it in `$$` instead of `'` helps avoid unncessary escaping. 

```sql
create table null_example (num_col number, char_col varchar(10)) 
as select * from (
    values (1, 'ABC'),
    (2, 'JKL'),
    (null, 'QRS'),
    (3, null)
    );
```

null can not be equated to anything. 

```sql
select num_col, char_col
from null_example
where num_col < 3; -- does not include rows where num_col is null
```

```sql
select num_col, char_col
from null_example 
where nvl(num_col,0) < 3; -- nvl substitutes null encountered with the specified value
```

`:daterange` `:datebucket` after including this in query, snowsight adds a menu to choose the date range. 

one can build custom filters using manage filters. 

1. inner join
2. left outer join
3. right outer join
4. cross join

```sql
select 
    years.yearnum, qtrs.qtrname, qtrs.startmonth, qtrs.endmonth
from (values (2020), (2021), (2022)) as years (yearnum)
cross join (values ('Q1',1,3), ('Q2',4,6), ('Q3',7,9),('Q4',10,12)) as qtrs (qtrname, startmonth, endmonth)
order by 1,2;
```

self-referencing foreign key. 

```sql
alter table employee add column birth_nationkey integer;
alter table employee add column current_nationkey integer;
update employee set birth_nationkey = empid - 1000, current_nationkey = empid - 999;
```

1. union - removes duplicates
2. union all - keeps duplicates
3. intersect
4. except | minus
5. (A union B) except (A intersect B) | (A except B) union (B except A)

When using set operations, only one query should have the order by clause, and it must use the column names from query 1. 


<br/><br/>

`varchar (n_chars)` - can store up to 16 MB
`number(38, 0)` - 38 digits
-  precision: total digits
-  scale: digits after decimal

`date`
`time`
`timestamp`
- `timestamp_ntz`
- `timestamp_ltz`
- `timestamp_tz`

`boolean`
`variant`
`array` - variable length array of `variant` values. 
`object` - keys are `varchar` and values are of `variant` type


<br/><br/>

```sql
select 'my string''s are lightly complex' as my_string
select $$my strings are complex '''$$
```

```sql
show parameters like 'timez%';
alter session set timezone='America/New_York';
select current_date, current_time, current_timestamp;

show parameters like 'date_output%';
alter session set date_output_format='MM/DD/YYYY';
```

```sql
select 1::variant, 'abc'::variant, current_date::variant;
select typeof('this is a character string'::variant); -- VARCHAR
select typeof(false::variant); -- BOOLEAN
```

```sql
select [123, 'ABC', current_time] as my_array;
select value from table(flatten(input=>[123, 'ABC', current_time]));
```

```sql
select key, value
from table(
    flatten(
        {'new_years' : '01/01', 
         'independence_day' : '07/04',
         'christmas' : '12/25'}
    )
);
```

```sql
insert overwrite into person -- overwrite removes all rows first and then inserts
(first_name, last_name, birth_date, eye_color, occupation, years_of_education)
values
    ('Bob','Smith','22-JAN-2000','brown','teacher', 18),
    ('Gina','Peters','03-MAR-2001','green','student', 12),
    ('Tim','Carpenter','09-JUL-2002','blue','salesman', 16),
    ('Kathy','Little','29-AUG-2001','brown','professor', 20),
    ('Sam','Jacobs','13-FEB-2003','blue','lawyer', 18);


insert into person 
(first_name, last_name, birth_date, eye_color, occupation, children, years_of_education)
select 
    'Sharon' as first_name, 
    last_name, birth_date, eye_color, 
    'doctor' as occupation, 
    ['Sue'::variant, 'Shawn'::variant] as children,
    20 as years_of_education
from person
where first_name = 'Tim' and last_name = 'Carpenter';
```

```sql
delete from person where first_name = 'Sam' and last_name = 'Jacobs';

delete from person
using employee
where employee.emp_name = concat(person.first_name, ' ', person.last_name);
```

Time Travel
```sql
insert into employee
select * from employee at(offset => -600)
where emp_name = 'Greg Carpenter';
```

```sql
update person
set occupation = 'musician', eye_color = 'grey'
where first_name = 'Kathy' and last_name = 'Little';

update person as p
set occupation = 'boss'
from employee as e
where e.emp_name = concat(p.first_name, ' ', p.last_name) and e.mgr_empid is null;
```

```sql
alter session set error_on_nondeterministic_update=true; 
-- after this, any multijoined updates fail. 

update person as p
set p.years_of_education = e.empid - 1000
from employee as e
where e.empid < 1003;
-- rows from person p, map to more than 1 row in employee, then it results in multijoined updates.
```

```sql
merge into person as p
using person_refresh as pr -- using specifies the source
on p.first_name = pr.fname and p.last_name = pr.lname
when matched and pr.remove = 'yes' then
    delete
when matched then 
    update set p.birth_date = pr.dob, p.eye_color = pr.eyes, p.occupation = pr.profession
when not matched then 
    insert (first_name, last_name, birth_date, eye_color, occupation)
    values (pr.fname, pr.lname, pr.dob, pr.eyes, pr.profession);
-- returns inserted, updated, deleted row counts
```

<br/><br/>
<br/><br/>


## Foundations 2: Chapter 6-

Chapters: 
- Data Generation, Conversion, and Manipulation; 
- Grouping and Aggregates


`char` `concat` `upper` `lower` `initcap` 
`ltrim` `rtrim` `trim` `length` 
`translate` `position` `substring` 
`startswith` `endswith` `contains`

`||`

`pi` `power` `mod` `sign` `abs`
`trunc` `round` `floor` `ceil`


`cast` `::` 
`to_decimal` `to_date`
`random` `seq1`
`date_from_parts` `time_from_parts` `timestamp_from_parts`
`date_trunc` `dateadd`
`dayname` `monthname`
`date_part`

Aggregate functions: `min` `max` `count` `sum` `avg` `count_if`
`listagg`

```sql
select concat('I spent ',char(8364),'539 in Paris');

select upper(str.val), lower(str.val), initcap(str.val)
from (values ('which case is best?')) as str(val);

select reverse('?siht daer uoy nac');

select 
    length(ltrim(str.val)) as str1_len, 
    length(rtrim(str.val)) as str2_len, 
    length(trim(str.val)) as str3_len
from (values ('    abc    ')) as str(val);
```

```sql
select translate('(857)-234-5678','()-',''); -- 8572345678
select translate('AxByCz','ABC','XYZ'); -- XxYyZz
```

```sql
select 
    position('here',str.val) as pos1,
    position('here',str.val,10) as pos2,
    position('nowhere',str.val) as pos3
from (values ('here, there, and everywhere')) as str(val);
```

```sql
select 
    substr(str.val, 1, 10) as start_of_string, 
    substr(str.val, 11) as rest_of_string
from (values ('beginning ending')) as str(val);

select 
    substr(str.val, position('every',str.val))
from (values ('here, there, and everywhere')) as str(val);
```

```sql
select str.val
from (values ('here, there, and everywhere')) as str(val)
where startswith(str.val,'here');
where endswith(str.val,'where');
where contains(str.val,'there');
```


```sql
select 
    10 as radius, 
    2 * 3.14159 * 10 as circumference,
    pi() * power(10,2) as area;

select mod(70, 9); -- gives reminder.

select sign(-7.5233), abs(-7.5233);

select trunc(6.49), round(6.49, 1), floor(6.49), ceil(6.49);
```


<br/><br/>



```sql
select 
    cast(str.val as number(7,2)) as cast_val, 
    str.val::number(7,2) as cast_opr_val, 
    to_decimal(str.val,7,2) as to_dec_val
from (values ('15873.26')) as str(val);


select to_decimal(str.val,'$99999.99',7,2) as to_dec_val
from (values ('$15873.26')) as str(val);

select 
    try_to_decimal(str.val,'$99999.99',7,2) as good,
    try_to_decimal(str.val,'999.9',4,2) as bad
from (values ('$15873.26')) as str(val);
```

```sql
select random() from table(generator(rowcount => 5));
select seq1() from table(generator(rowcount => 5));

select 
    to_date('01/' || to_char(seq1() + 1) || '/2023','DD/MM/YYYY') as first_of_month
from table(generator(rowcount => 12));
```

```sql
select to_timestamp('04-NOV-2022 18:48:56','DD-MON-YYYY HH24:MI:SS') as now;
show parameters like 'timestamp_out%'; -- YYYY-MM-DD HH24:MI:SS.SSS
alter session set timestamp_output_format = 'MM/DD/YYYY HH12:MI:SS AM TZH'; --  11/03/2022 04:42:47 PM -0700

select 
    date_from_parts(2023, 3, 15) as my_date,
    time_from_parts(10, 22, 47) as my_time;
```

```sql
select date_from_parts(2024, seq1() + 2, 0) as month_end
from table(generator(rowcount => 12));
-- 0 previous day (1 day)
-- 1 move backward 2 days
```

```sql
select 
    date_trunc('YEAR',dt.val) as start_of_year,
    date_trunc('MONTH',dt.val) as start_of_month,
    date_trunc('QUARTER',dt.val) as start_of_quarter
from (values (to_date('26-MAY-2023','DD-MON-YYYY'))) as dt(val);
```

```sql
select 
    dateadd(month, 1, to_date('01-JAN-2024','DD-MON-YYYY')) as date1,
    dateadd(month, 1, to_date('15-JAN-2024','DD-MON-YYYY')) as date2,
    dateadd(month, 1, to_date('31-JAN-2024','DD-MON-YYYY')) as date3;

select dateadd(year, -1, to_date('29-FEB-2024','DD-MON-YYYY')) new_date;

select dayname(current_date), monthname(current_date);
```

```sql
select 
    date_part(year, dt.val) as year_num,
    date_part(quarter, dt.val) as qtr_num,
    date_part(month, dt.val) as month_num,
    date_part(week, dt.val) as week_num
from (values(to_date('24-APR-2023','DD-MON-YYYY'))) as dt(val);

select 
    date_part(hour, dt.val) as hour_num,
    date_part(minute, dt.val) as min_num,
    date_part(second, dt.val) as sec_num,
    date_part(nanosecond, dt.val) as nsec_num
from (values(current_timestamp)) as dt(val);
```

```sql
select 
    datediff(year, dt.val1, dt.val2) num_years,
    datediff(month, dt.val1, dt.val2) num_months,
    datediff(day, dt.val1, dt.val2) num_days,
    datediff(hour, dt.val1, dt.val2) num_hours
from (values (to_date('12-FEB-2022','DD-MON-YYYY'),to_date('06-MAR-2023','DD-MON-YYYY'))) as dt(val1, val2);
```

```sql
select try_cast('09-23-2023' as date);

select 
    '09/23/2023'::date date_val,
    '23-SEP-2023'::timestamp tmstmp_val,
    '123.456'::number(6,3) num_val;
```

```sql
select 
    count_if(1992 = date_part(year, o_orderdate)) num_1992,
    count_if(1995 = date_part(year, o_orderdate)) num_1995
from orders;
```

```sql
select 
    r.r_name,
    listagg(n.n_name,',') within group (order by n.n_name) as nation_list
from region r inner join nation n on r.r_regionkey = n.n_regionkey
group by r.r_name;
```

```sql
select 
    date_part(year, o.o_orderdate) as year,
    datediff(month, o.o_orderdate, l.l_shipdate) as months_to_ship,
    count(*)
from orders o inner join lineitem l on o.o_orderkey = l.l_orderkey
where o.o_orderdate >= '01-JAN-1997'::date
group by date_part(year, o.o_orderdate), datediff(month, o.o_orderdate, l.l_shipdate)
order by 1,2;
```

`group by all` - everything in select that is not aggregate. 

```sql
select n.n_name, c.c_mktsegment, count(*)
from customer c inner join nation n on c.c_nationkey = n.n_nationkey
where n.n_regionkey = 1
group by rollup(n.n_name, c.c_mktsegment) -- rolls up one col at a time. you won't get totals by mktsegment
order by 1,2;

select n.n_name, c.c_mktsegment, count(*)
from customer c inner join nation n on c.c_nationkey = n.n_nationkey
where n.n_regionkey = 1
group by cube(c.c_mktsegment, n.n_name) -- rolls up all variations. you will get totals by mktsegment as well
order by 1,2;

select 
    n.n_name, c.c_mktsegment, count(*),
    grouping(n.n_name) name_sub,
    grouping(c.c_mktsegment) mktseg_sub
from customer c inner join nation n on c.c_nationkey = n.n_nationkey
where n.n_regionkey = 1
group by cube(c.c_mktsegment, n.n_name)
order by 1,2;
```

`grouping` - returns 0 if associated col is included in subtotals; 1 otherwise. 