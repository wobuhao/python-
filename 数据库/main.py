from data_define import Record
from file_define import FileReader, TextFileeReader, JsonFileReader
from pymysql import Connection

conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='hy120120',
    #autocommit=True
)
conn.select_db('test')
cursor = conn.cursor()

# 获取数据
# text_file_reader = TextFileeReader('F:/python/1、Python快速入门（8天零基础入门到精通）/资料/第13章资料/2011年1月销售数据.txt')
# json_file_reader = JsonFileReader('F:/python/1、Python快速入门（8天零基础入门到精通）/资料/第13章资料/2011年2月销售数据JSON.txt')
#
# jan_data: list[Record] = text_file_reader.read_data()
# feb_data: list[Record] = json_file_reader.read_data()
# all_data = list(jan_data) + list(feb_data)
# new_data = list()
# for z in all_data:
#     new_data.append((z.date, z.order_id, z.money, z.province))
#     # print(f"xx{z}, {type(z)}")
#
# try:
#     sql = "insert into orders1 values(%s, %s, %s, %s)"
#     cursor.executemany(sql, new_data)
#     conn.commit()
#     print("成功")
# except Exception as e:
#     conn.rollback()
#     print(f"错误消息{e}")


# 读取数据
cursor.execute("select * from orders1")

results: tuple = cursor.fetchall()

for r in results:
    print(str(r[0]))

cursor.close()
conn.close()
