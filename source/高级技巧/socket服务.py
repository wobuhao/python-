import socket

socket_server = socket.socket()
# 绑定socket_server到指定IP和地址
socket_server.bind(("localhost", 8888))

# 监听端口 listen方法接收一个整数参数，表示接受连接数量
socket_server.listen(1)

# 等待客户端连接 accept()方法是阻塞的方法，等待客户端的连接，如果没有连接，就卡在这一行不向下执行
# result = socket_server.accept()
# conn = result[0]    # 客户端和服务端的连接对象
# address = result[1] # 客户端的地址信息
# 简写方式 可以通过 变量1, 变量2 = socket_server.accept()的形式，直接接受二元元祖内的两个元素
conn, address = socket_server.accept()
print(f"接收到了客户端的连接，客户端的信息是：{address}")

while True:
    # 接受客户端信息
    data: str = conn.recv(1024).decode("UTF-8")
    print(f"客户端发来的信息是：{data}")
    # recv 接受的参数是缓存区大小，一般给1024即可
    # recv 方法的返回值是一个字节数组，也就是bytes对象，不是字符串，可以通过decode方法通过UTF-8编码，将字节数组转换为字符串对象

    # 发送回复消息
    msg = input("请输入你要和客户端回复的消息：")  # 通过encode方法将字符串对象转为字节数组
    if msg == 'exit':
        break
    conn.send(msg.encode("UTF-8"))

# 关闭连接
conn.close()
socket_server.close()
