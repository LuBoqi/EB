import socket


class Server(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('0.0.0.0', 9999))  # 使用0.0.0.0可监听所有可用的网络接口

    def listen(self):
        self.server_socket.listen(50)
        self.client_socket, self.client_address = self.server_socket.accept()
        while True:
            data = self.client_socket.recv(1024)
            # if not data:
            #     break
            print(f"收到消息: {data.decode()}")

    def close(self):
        # 关闭连接
        self.client_socket.close()
        self.server_socket.close()
