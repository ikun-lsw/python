import socket

# 1、创建客户端套接字对象
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2、和服务器端套接字建立连接(参数必须是一个元祖)
tcp_client_socket.connect(('192.168.31.139', 8080))
# 3、发送数据
tcp_client_socket.send('hell, itheima'.encode(encoding='utf-8'))
# 4、接收数据
recv_data = tcp_client_socket.recv(1024).decode('utf-8')
print(recv_data)
# 5、关闭客户端套接字
tcp_client_socket.close()
