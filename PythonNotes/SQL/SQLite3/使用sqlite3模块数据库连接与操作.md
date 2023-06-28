python使用`sqlite3`

- ```
  import sqlite3
  sql_path = "./sqlitedb"
  if not os.path.exists(sql_path):
  	# 创建sqlitedb
  	connection= sqlite3.connect(sql_path)
      connection.commit()
  connection = sqlite3.connect(sql_path, check_same_thread=False)
  cursor = connection.cursor()
  
  # 使用Demo
  sql = "SELECT * FROM 表名"
  try:
  	cursor.execute(sql)
  	tables = cursor.fetchall()
  	connection.commit()
  except Exception as err:
  	connection.rollback()
  ```

  

