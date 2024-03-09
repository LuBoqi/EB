import threading
import message
from message import Message
from database import ChatLogs
import socket
import time
from server import cmd


class Client:
    def __init__(self, server_ip, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((server_ip, port))
        self.id = None
        self.pwd = None
        self.now_msg = Message(self.id)
        self.send_msg = Message(self.id)
        self.friends = []
        self.chat_logs = ChatLogs('chat_logs.csv')

    def login(self, id, pwd):
        self.id = id
        self.pwd = pwd
        self.send('password', self.pwd)
        print('try login...')
        feedback = self.client_socket.recv(1024).decode()
        feedback = [data for data in feedback.split('\r\n\r\n') if data]
        for pack in feedback:
            self.now_msg.de_code(pack)
            if self.now_msg.sender == 'password':
                print('登陆结果:', self.now_msg.content)
                if self.now_msg.content != 'True':
                    return False
        return True

    def send(self, receiver, msg):
        self.client_socket.send(self.now_msg.en_code(self.id, receiver, msg))

    def receive(self):
        try:
            while True:
                self.send('1', 'hello')
                feedback = self.client_socket.recv(1024).decode()
                feedback = [data for data in feedback.split('\r\n\r\n') if data]
                for pack in feedback:
                    self.now_msg.de_code(pack)
                    if self.now_msg.sender not in cmd and self.now_msg.receiver == self.id:
                        print('收到消息:', self.now_msg.content)
                time.sleep(1)
        except Exception as e:
            print("Error:", e)
        finally:
            exit(-2)

    def close(self):
        self.client_socket.close()

    def get_friends(self):  # 推荐参照'__main__'使用线程刷新，后续添加在线人员判定于此函数
        try:
            while True:
                self.send('friends', self.pwd)
                feedback = self.client_socket.recv(1024).decode()
                feedback = [data for data in feedback.split('\r\n\r\n') if data]
                for pack in feedback:
                    self.now_msg.de_code(pack)
                    if self.now_msg.sender == 'friends':
                        self.friends = [data for data in self.now_msg.content.split('\r') if data]
                # print(self.friends)
                time.sleep(5)
        except Exception as e:
            print("Error:", e)
        finally:
            exit(-1)


if __name__ == '__main__':
    client = Client('127.0.0.1', 8989)
    have_login = False
    while True:
        if not have_login:
            have_login = client.login('1', 'password1')
        elif client.id == '0':
            print('欢迎进入管理员帐号')
        else:
            print('进入服务')
            friend_thread = threading.Thread(target=client.get_friends())
            receive_thread = threading.Thread(target=client.receive())
            # receive_thread.start()
            # friend_thread.start()
            client.send('1', message.get_time_string())
        time.sleep(0.1)
