import socket
import threading
from database import ChatLogs, User_info, Friend_list
from message import Message

cmd = ['password', 'friends', 'register']


class Server(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((ip, port))
        self.chat_logs = ChatLogs('chat_logs.csv')
        self.log_in = User_info('user_info.csv')
        self.friend_list = Friend_list('friend_list.csv')
        self.msg = Message('server')
        self.clients = []

    def handle_client(self, client_socket, client_address):
        print("连接来自:", client_address)
        client_name = ':'.join(str(item) for item in client_address)
        this_msg = Message(client_name)
        land_error_time = 1
        try:
            while True:
                if land_error_time > 5:  # 密码输错5次就关闭链接
                    client_socket.sendall(self.msg.en_code('password', client_name, '密码错误！！！'))
                    client_socket.close()
                    break
                received_data = client_socket.recv(1024).decode()
                received_data = [data for data in received_data.split('\r\n\r\n') if data]
                for pack in received_data:
                    this_msg.de_code(pack)
                    if this_msg.receiver == 'password':  # 登陆密码判定
                        result = self.log_in.get_user(this_msg.sender, this_msg.content) is not None
                        if not result:
                            land_error_time = land_error_time + 1
                        else:
                            client_name = this_msg.sender
                            self.clients.append([client_socket, this_msg.sender])
                        print('{}时刻{}使用密码{}'.format(this_msg.time, this_msg.sender, this_msg.content))
                        client_socket.sendall(self.msg.en_code('password', client_name, str(result)))
                    elif this_msg.receiver == 'register':
                        id_name = this_msg.sender
                        pwd = this_msg.content
                        user_id, user_name = id_name.split("@")[0], id_name.split("@")[1]
                        result = self.log_in.ID_check(user_id)
                        if result:
                            self.log_in.insert_user(user_id, user_name, pwd)
                            self.log_in = User_info('user_info.csv')
                        else:
                            print("register fail!")
                        client_socket.sendall(self.msg.en_code('register', client_name, str(result)))
                    elif this_msg.receiver == 'friends':  # 请求好友列表
                        print('{}请求好友列表'.format(this_msg.sender))
                        friends = self.friend_list.get_friends(this_msg.sender)
                        tmp_msg = '\r'
                        for friend in friends:
                            tmp_msg = tmp_msg + friend + '\r'
                        client_socket.sendall(self.msg.en_code('friends', client_name, tmp_msg))
                    else:  # 发送消息
                        print('{}时刻{}向{}发送{}'.format(this_msg.time, this_msg.sender,
                                                          this_msg.receiver, this_msg.content))
                        if this_msg.receiver == '0':  # 群发消息
                            for client in self.clients:
                                if client[1] != this_msg.sender:
                                    client[0].sendall(self.msg.en_code(this_msg.sender,
                                                                       client[1], this_msg.content))
                        else:  # 私聊发送
                            for client in self.clients:
                                if client[1] == this_msg.receiver:
                                    client[0].sendall(self.msg.en_code(this_msg.sender,
                                                                       this_msg.receiver, this_msg.content))
                                    break
        except Exception as e:
            print("Error:", e)
            self.clients = [client for client in self.clients if client[1] != client_name]
            client_socket.close()
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
