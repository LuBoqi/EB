import socket


# 创建一个IPv4 TCP socket
class ClientSocket:
    def __init__(self, server_ip, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('服务端IP地址', 9999))  # 替换为实际的服务端IP地址

    def send(self, msg):
        self.client_socket.send(msg.encode())

    def close(self):
        # 关闭连接
        self.client_socket.close()
