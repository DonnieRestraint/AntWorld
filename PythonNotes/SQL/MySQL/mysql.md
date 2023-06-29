# MYSQL数据库与SQL

- `MySQL`数据库的基本操作

```mysql
# http://c.biancheng.net/mysql/30/
```

- 数据库设计

```
# 逻辑结构设计
https://zhuanlan.zhihu.com/p/50448594
# E-R(实体关系图)
https://blog.csdn.net/Hell_potato777/article/details/126603314
# 数据库设计规范
https://blog.csdn.net/weixin_42382291/article/details/107517280
https://blog.csdn.net/weixin_42382291/article/details/107532614
https://blog.csdn.net/weixin_42382291/article/details/107555824
https://blog.csdn.net/weixin_42382291/article/details/107610637
# 数据库三范式
https://worktile.com/kb/ask/30501.html
```

- 重置密码

```mysql
alter user user() identified by "密码";
```

- 数据库基本操作

```mysql
# 显示所有数据库
SHOW DATABASES;
# 选择数据库；
USE '数据库名';
# 显示所有表
SHOW TABLES;

# 创建数据库
# http://c.biancheng.net/view/2413.html
 CREATE DATABASE '数据库名';
 # 创建数据表
 CREATE TABLE '表名' (
     id INT(11), 
     name VARCHAR(25)
 );
```



[TOC]





## 一 SQL 简介

SQL 包含以下 4 部分：

#### 1）数据定义语言（Data Definition Language，DDL）

用来创建或删除数据库以及表等对象，主要包含以下几种命令：

- DROP：删除数据库和表等对象
- CREATE：创建数据库和表等对象
- ALTER：修改数据库和表等对象的结构

#### 2）数据操作语言（Data Manipulation Language，DML）

用来变更表中的记录，主要包含以下几种命令：

- SELECT：查询表中的数据
- INSERT：向表中插入新数据
- UPDATE：更新表中的数据
- DELETE：删除表中的数据

#### 3）数据查询语言（Data Query Language，DQL）

用来查询表中的记录，主要包含 SELECT 命令，来查询表中的数据。

#### 4）数据控制语言（Data Control Language，DCL）

用来确认或者取消对数据库中的数据进行的变更。除此之外，还可以对数据库中的用户设定权限。主要包含以下几种命令：

- GRANT：赋予用户操作权限
- REVOKE：取消用户的操作权限
- COMMIT：确认对数据库中的数据进行的变更
- ROLLBACK：取消对数据库中的数据进行的变更


下面是一条 SQL 语句的例子，该语句声明创建一个名叫 students 的表：

```
CREATE TABLE students (
    student_id INT UNSIGNED,
    name VARCHAR(30) ,
    sex CHAR(1),
    birth DATE,
    PRIMARY KEY(student_id)
);
```

该表包含 4 个字段，分别为 student_id、name、sex、birth，其中 student_id 定义为表的主键。

现在只是定义了一张表格，但并没有任何数据，接下来这条 SQL 声明语句，将在 students 表中插入一条数据记录：

```
INSERT INTO students (student_id, name, sex, birth)
VALUES (41048101, 'C语言中文网MySQL教程', '1', '2013-02-14');
```

执行完该 SQL 语句之后，students 表中就会增加一行新记录，该记录中字段 student_id 的值为“41048101”，name 字段的值为“C语言中文网MySQL教程”。sex 字段值为“1”，birth 字段值为“2013-02-14”。

再使用 SELECT 查询语句获取刚才插入的数据，如下：

```
SELECT name FROM students WHERE student_id=41048101;
```

## 二 SQL 基本书写规则

- SQL 语句要以分号`;`结尾
- SQL 语句不区分大小写

- 一般书写习惯为：
  - 关键字大写
  - 数据库名、表名和列名等小写
- 常数的书写方式是固定的。字符串、日期或者数字
  - 字符串：'abc'等
  - 日期：'26 Jan 2010' 或者'10/01/26'或者'2020-01-26'等
  - 数字：100等

```
CREATE TABLE tb_emp1
(
id INT(11),
name VARCHAR(25)
);
```

- 列名不是字符串，不能使用**单引号**''。在MySQL中可以用**倒引号**`把表名和列名括起来，如下：

```
INSERT INTO `tb_emp1` (`id`, `name`) VALUES (1, 'test');
```

## MySQL数据库相关操作

#### 1）查询数据库

```mysql
SHOW DATABASES [LIKE '数据库名'];
# LIKE 从句是可选项，用于匹配指定的数据库名称。LIKE 从句可以部分匹配，也可以完全匹配。
# 数据库名由单引号' '包围。
```

- ```mysql
  # LIKE从句
  # 完全匹配test
  LIKE 'test'
  # 包含test
  LIKE '%test%'
  # 以test开头
  LIKE 'test%'
  # 以test结尾
  LIKE '%test'
  
  # 例如：
  SHOW DATABASES LIKE 'TEST%';
  ```

  

#### 2）创建数据库

```mysql
CREATE DATABASE [IF NOT EXISTS] <数据库名>
[[DEFAULT] CHARACTER SET <字符集名>] 
[[DEFAULT] COLLATE <校对规则名>];

# <数据库名>：创建数据库的名称。MySQL 的数据存储区将以目录方式表示 MySQL 数据库，因此数据库名称必须符合操作系统的文件夹命名规则，不能以数字开头，尽量要有实际意义。注意在 MySQL 中不区分大小写。
# IF NOT EXISTS：在创建数据库之前进行判断，只有该数据库目前尚不存在时才能执行操作。此选项可以用来避免数据库已经存在而重复创建的错误。
# [DEFAULT] CHARACTER SET：指定数据库的字符集。指定字符集的目的是为了避免在数据库中存储的数据出现乱码的情况。如果在创建数据库时不指定字符集，那么就使用系统的默认字符集。
# [DEFAULT] COLLATE：指定字符集的默认校对规则。
```

- ```mysql
  # 将数据库命名为 test_db_char，指定其默认字符集为 utf8，默认校对规则为 utf8_chinese_ci（简体中文，不区分大小写）
  CREATE DATABASE IF NOT EXISTS test_db_char
  DEFAULT CHARACTER SET utf8
  DEFAULT COLLATE utf8_chinese_ci;
  ```

- 查看数据库的定义声明

  ```mysql
  SHOW CREATE DATABASE test_db_char;
  ```



#### 3）修改数据库

```mysql
ALTER DATABASE [数据库名] { 
[ DEFAULT ] CHARACTER SET <字符集名> |
[ DEFAULT ] COLLATE <校对规则名>};

# ALTER DATABASE 用于更改数据库的全局特性。
# 使用 ALTER DATABASE 需要获得数据库 ALTER 权限。
# 数据库名称可以忽略，此时语句对应于默认数据库。
# CHARACTER SET 子句用于更改默认的数据库字符集。
```

- ```mysql
  # 将数据库 test_db 的指定字符集修改为 gb2312，默认校对规则修改为 gb2312_unicode_ci
  ALTER DATABASE test_db
  DEFAULT CHARACTER SET gb2312
  DEFAULT COLLATE gb2312_chinese_ci;
  ```



#### 4）删除数据库

```mysql
DROP DATABASE [ IF EXISTS ] <数据库名>;

# <数据库名>：指定要删除的数据库名。
# IF EXISTS：用于防止当数据库不存在时发生错误。
# DROP DATABASE：删除数据库中的所有表格并同时删除数据库。使用此语句时要非常小心，以免错误删除。如果要使用 DROP DATABASE，需要获得数据库 DROP 权限。
```

#### 5）选择数据库

```mysql
USE <数据库名>;
```

#### 6）注释

```mysql
# 控制台注释
一
#注释
二
-- 注释
三
/*
  第一行注释内容
*/
```

- ```mysql
  SELECT DISTINCT product_id, purchase_price
  -- 从结果中删除重复行,相当于product_id, purchase_price的组合索引
  FROM Product;
  ```

  

#### 7） 大小写规则

```txt
MySQL 
在Windows中的文件名不区分大小写
而Linux中的文件名是区分大小写
造成数据库迁移之间的问题

故在阿里巴巴Java开发手册的MySql建库建表规约里提到：
	数据库名、表名和字段名都不允许出现任何大写字母
	表名、字段名必须使用小写字母或数字，禁止出现数字开头，禁止两个下划线中间只出现数字

```

#### 8）MySQL系统帮助

```mysql
HELP 查询内容

# 其中，查询内容为要查询的关键字。
# 查询内容中不区分大小写。
# 查询内容中可以包含通配符“％”和“_”，效果与 LIKE 运算符执行的模式匹配操作含义相同。例如，HELP 'rep％' 用来返回以 rep 开头的主题列表。
# 查询内容可以使单引号引起来，也可以不使用单引号，为避免歧义，最好使用单引号引起来。
```

- ```mysql
  HELP contents; # 命令查看帮助文档的目录列表
  
  HELP Data Types; # 命令查看所支持的数据类型
  
  HELP INT;	# 命令查看所支持的数据类型INT的帮助描述
  
  HELP CREATE TABLE 	# 命令查看创建表的语法
  ```

- ```txt
  MySQL 提供了 4 张数据表来保存服务端的帮助信息，即使用 HELP 语法查看的帮助信息。
  help_category：关于帮助主题类别的信息
  help_keyword：与帮助主题相关的关键字信息
  help_relation：帮助关键字信息和主题信息之间的映射
  help_topic：帮助主题的详细内容
  ```

  

