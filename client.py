from message import Message
import socket
import time


class Client:
    def __init__(self, server_ip, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((server_ip, port))

    def land(self, name, pwd):
        self.client_socket.sendall('land'.encode())

    def send(self, msg):
        self.client_socket.send(msg.encode())

    def receive(self):
        return client.client_socket.recv(1024).decode()

    def close(self):
        # 关闭连接
        self.client_socket.close()


if __name__ == '__main__':
    client = Client('127.0.0.1', 8989)
    while True:
        client.land('admin', 'admin')
        client.send(str(time.time()))
        print(client.receive())
        time.sleep(1)
