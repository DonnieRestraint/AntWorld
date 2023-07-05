- sqlite3 中的占位符 ？

  ```
  占位符？中的语句不会表示解析成sql的关键字
  ```
  
  
  
- `SQLite`有五种类型：integer、real、text、blob、null。

  ```
  Null：该值为 NULL 值
  Integer：该值是有符号整数（1、2、3 等）
  Real：该值为浮点值，存储为 8 字节 IEEE 浮点数
  Text：该值为文本字符串，使用数据库编码（UTF-8、UTF-16BE）存储
  BLOB (Binary Large Object)：该值是一个数据块，完全按照输入的方式存储
  ```

  

  ```sqlite
  # 创建基本表
  CREATE TABLE 表名  (id int, name text, score real);
  # 创建表并带约束的表
  CREATE TABLE 表名 (id int primary key, name text);
  # 创建临时表， 临时表是暂时存活，连接断开就会自动销毁。
  CREATE TEMP TABLE stu  (id int, name text, score real);	
  ```

- 表查询

  ```sqlite
  # 查询所有表名
  SELECT name FROM sqlite_master WHERE type='table' and name!='sqlite_sequence';
  # 查询排序后的所有表名
  SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;
  # 查询过滤后的所有表名
  SELECT name FROM sqlite_master WHERE type='table' and name !='表名';
  ```

- 删除表

  ```sqlite
  DROP TABLE 表名;
  ```
  
- 查询表的所有字段

  ```sqlite
  PRAGMA table_info(表名);
  ```

- 修改表

  ```sqlite
  # 增加一个无初始值字段：
  alter table 表名 add column <字段名> <类型>;
  # 增加一个有初始值字段：
  alter table stu add column <字段名> <类型> default value;
  # 修改表名：
  alter table <tablename_old> rename to <tablename_new>
  ```


- 查询数据

  ```
  SELECT id, name FROM 表名 WHERE id=? OR name=?;
  ```

- 插入一条数据

  ```
  INSERT INTO 表名 (字段1,字段2,...) VALUES (value1,value2,...);
  ```

- 删除一条数据

  ```
  DELETE FROM 表名 WHERE id=?;
  ```

- ORM执行的SQL

  ```python
  sql = """INSERT INTO {table_name} (field1,field2) VALUES (?,?,?)""".format(table_name="表名",field1="字段1",field2="字段2")
  ```

  

### 摘取相关语法

```
https://zhuanlan.zhihu.com/p/496160310
```

```sqlite
# 创建表
CREATE TABLE database_name.table_name(
   column1_name datatype  PRIMARY KEY(one or more columns),
   column2_name datatype,
   column3_name datatype,
   .....
   columnN_name datatype,
);
# 删除表
DROP TABLE database_name.table_name;
```

- 增删改查

```
INSERT INTO TABLE_NAME [(column1, column2, column3,...columnN)]  
VALUES (value1, value2, value3,...valueN);

DELETE FROM table_name
WHERE [condition];

UPDATE table_name
SET column1 = value1, column2 = value2...., columnN = valueN
WHERE [condition];

SELECT column1, column2, columnN FROM table_name;
SELECT * FROM table_name;
```

```sql
# WHERE
SELECT column1, column2, columnN 
FROM table_name
WHERE [condition]

# AND和OR
SELECT column1, column2, columnN 
FROM table_name
WHERE [condition1] AND [condition2]...AND [conditionN];

# LIKE
SELECT column_list 
FROM table_name
-- '%XXXX%',  '%XXXX'
WHERE column LIKE 'XXXX%'

SELECT column_list 
FROM table_name
-- '_XXXX_',  'XXXX_'
WHERE column LIKE '_XXXX'

# LIMIT
SELECT column1, column2, columnN 
FROM table_name
LIMIT [no of rows]

SELECT column1, column2, columnN 
FROM table_name
LIMIT [no of rows] OFFSET [row num]

# ORDER BY
SELECT column-list 
FROM table_name 
[WHERE condition] 
[ORDER BY column1, column2, .. columnN] [ASC | DESC];

# GROUP BY
SELECT column-list
FROM table_name
WHERE [ conditions ]
GROUP BY column1, column2....columnN
ORDER BY column1, column2....columnN

# Having
SELECT column1, column2
FROM table1, table2
WHERE [ conditions ]
GROUP BY column1, column2
HAVING [ conditions ]
ORDER BY column1, column2

# Distinct
SELECT DISTINCT column1, column2,.....columnN 
FROM table_name
WHERE [condition]

# CROSS JOIN
SELECT ... FROM table1 CROSS JOIN table2 ...
# INNER JOIN
SELECT ... FROM table1 [INNER] JOIN table2 ON conditional_expression ...
# OUTER JOIN
SELECT ... FROM table1 LEFT OUTER JOIN table2 ON conditional_expression ...

# Unios
SELECT column1 [, column2 ]
FROM table1 [, table2 ]
[WHERE condition]
UNION
SELECT column1 [, column2 ]
FROM table1 [, table2 ]
[WHERE condition]

# 视图
CREATE [TEMP | TEMPORARY] VIEW view_name AS
SELECT column1, column2.....
FROM table_name
WHERE [condition];
# 删除视图
DROP VIEW view_name;

# 事务
sqlite> BEGIN;
sqlite> DELETE FROM COMPANY WHERE AGE = 25;
sqlite> ROLLBACK;

sqlite> BEGIN;
sqlite> DELETE FROM COMPANY WHERE AGE = 25;
sqlite> COMMIT;

# 函数
SQLite COUNT 函数：SQLite COUNT 聚集函数是用来计算一个数据库表中的行数。
SQLite MAX 函数：SQLite MAX 聚合函数允许我们选择某列的最大值
SQLite MIN 函数： SQLite MIN 聚合函数允许我们选择某列的最小值。
SQLite AVG 函数： SQLite AVG 聚合函数计算某列的平均值。
SQLite SUM 函数： SQLite SUM 聚合函数允许为一个数值列计算总和。
SQLite RANDOM 函数： SQLite RANDOM 函数返回一个介于 -9223372036854775808 和 +9223372036854775807 之间的伪随机整数。
SQLite ABS 函数： SQLite ABS 函数返回数值参数的绝对值。
SQLite UPPER 函数： SQLite UPPER 函数把字符串转换为大写字母。
SQLite LOWER 函数： SQLite LOWER 函数把字符串转换为小写字母
SQLite LENGTH 函数： SQLite LENGTH 函数返回字符串的长度。
SQLite sqlite_version 函数： SQLite sqlite_version 函数返回 SQLite 库的版

# 别名
SELECT column1, column2....
FROM table_name AS alias_name
WHERE [condition];

SELECT column_name AS alias_name
FROM table_name
WHERE [condition];

# 触发器
CREATE  TRIGGER trigger_name [BEFORE|AFTER] event_name 
ON table_name
BEGIN
 -- 触发器逻辑....
END;

CREATE  TRIGGER trigger_name [BEFORE|AFTER] UPDATE OF column_name 
ON table_name
BEGIN
 -- 触发器逻辑....
END;

# Alter
ALTER TABLE database_name.table_name RENAME TO new_table_name;
ALTER TABLE database_name.table_name ADD COLUMN column_def...;
```



