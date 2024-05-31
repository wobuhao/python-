import socket
socket_client = socket.socket()

# 连接到服务器
socket_client.connect(("localhost", 8888))

# 发送消息
while True:
    send_msg = input("请输入要发送的消息")
    if send_msg == 'exit':
        break
    socket_client.send(send_msg.encode("UTF-8"))
    recv_data = socket_client.recv(1024).decode("UTF-8")
    print(f"服务端回复的消息是：{recv_data}")


socket_client.close()
