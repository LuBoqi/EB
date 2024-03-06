import socket
import threading


class Server(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((ip, port))

    def handle_client(self, client_socket, client_address):
        print("连接来自:", client_address)
        try:
            while True:
                received_data = client_socket.recv(1024)
                print("接收到来自{}的消息: {}".format(client_address, received_data.decode()))
                # 假设服务器要回复客户端
                client_socket.sendall('Server received your message.'.encode())
        except Exception as e:
            print("Error:", e)
        finally:
            # 关闭客户端连接
            client_socket.close()

    def listen(self):
        self.server_socket.listen(5)
        try:
            while True:
                client_socket, client_address = self.server_socket.accept()
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
                client_thread.start()
        except KeyboardInterrupt:
            print('服务器停止运行')
        finally:
            self.server_socket.close()


if __name__ == '__main__':
    server = Server('127.0.0.1', 8989)
    server.listen()
