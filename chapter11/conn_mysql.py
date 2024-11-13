import pandas as pd
import pymysql

# 使用Python进行数据库连接测试
password = "000000"
conn = pymysql.connect(host="localhost", user="root", password=password, db="practive_database", charset="utf8")

# 查询语句
sql_query = 'select * from practive_database.user limit 5'
# 使用Pandas的方法读取数据
data = pd.read_sql(sql_query, con=conn)
# 关闭数据库连接
conn.close()
# 输出部分数据
print(data.head)
