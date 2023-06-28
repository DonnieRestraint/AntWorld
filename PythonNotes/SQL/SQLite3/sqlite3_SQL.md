- 查询`所有表`

  - ```sqlite
    SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;
    ```

- 查询`表名`所有字段

  - ```sqlite
    PRAGMA table_info(表名);
    ```

- 查询`某个表`

  - ```
    SELECT name FROM sqlite_master WHERE type='table' and name !='表名';
    ```

- 多条`SQL插入`

  - ```
    sql = INSERT INTO 表名(字段,字段...) VALUES (?,?...)
    cursor.execute(sql, data_list)
    connection.commit()
    ```

- `SQLite`有五种类型：integer、real、text、blob、null。
  - ```
    # 创建带约束的表
    CREATE TABLE 表名 (id int primary key, name text);
    ```

  - ```
    # 创建基本表
    CREATE TABLE 表名  (id int, name text, score real);
    # 创建临时表， 临时表是暂时存活，连接断开就会自动销毁。
    CREATE TEMP TABLE stu  (id int, name text, score real);	
    ```

- 修改表

  - ```
    # 增加一个无初始值字段：
    alter table 表名 add column <字段名> <类型>;
    # 增加一个有初始值字段：
    alter table stu add column <字段名> <类型> default value;
    # 修改表名：
    alter table <tablename_old> rename to <tablename_new>
    ```

    

