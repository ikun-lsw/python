# 导入模块
import socket

# 1.创建服务器端套接字对象
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(tcp_server_socket)
# 端口复用
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 2.绑定IP地址与端口号
tcp_server_socket.bind(('', 8012))

# 3.设置监听
tcp_server_socket.listen(128)

# 4.等待客户端连接
# print(tcp_server_socket.accept())
while True:
    try:
        new_socket, ip_port = tcp_server_socket.accept()
        # print(new_socket)  # 新服务器端套接字对象
        # print(ip_port)  # 客户端信息
        while True:
            try:
                # 5.接收客户端发过来的数据
                recv_data = new_socket.recv(1024)
                recv_data = recv_data.decode('gbk')
                print(f'{ip_port}客户端发来的数据:{recv_data}')
                content = input('服务器端消息：').encode('gbk')
                new_socket.send(content)
            except ConnectionError:
                print(f'{ip_port}客户端断开连接')
                break
    except:
        print('出错，退出服务器')
        break

# 7.关闭套接字对象
new_socket.close()
