"""
SQLITE3
"""

"""查询表, sqlite_sequence表：记录每个用户数据表的名字以及自动增长大整数主键字段的最大值"""
sqlite3_001 = """SELECT name FROM sqlite_master WHERE type='table' and name!='sqlite_sequence' ORDER BY name;"""


