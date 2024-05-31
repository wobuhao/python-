from pymysql import Connection
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='hy120120',
    autocommit=True  # 自动提交
)

print(f"{conn.get_server_info()}")
# 获取游标对象
cursor = conn.cursor()

# 选择数据库
conn.select_db('test')

# 使用游标对象执行sql语句
#cursor.execute("CREATE TABLE test_mysql(id INT, info VARCHAR(255))")

# 执行查询语句
cursor.execute("select * from student limit 2, 2")

# 获取查询结果
results: tuple = cursor.fetchall()
for r in results:
    print(r)

# 插入数据
cursor.execute("insert into student values(10006, \"张飞2\", 500)")

conn.commit()

# 关闭数据库连接
conn.close()
