from concurrent.futures import ThreadPoolExecutor

from message import Message
from database import ChatLogs
from server import cmd
import message
import socket
import time


class Client():
    def __init__(self, server_ip, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((server_ip, port))
        self.id = None
        self.pwd = None
        self.now_msg = Message(self.id)
        self.send_msg = Message(self.id)
        self.friends = []
        self.online_friends = []
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

    def register(self, user_id, user_name, pwd):
        id_name = user_id + '@' + user_name
        self.client_socket.send(self.now_msg.en_code(id_name, "register", pwd))
        feedback = self.client_socket.recv(1024).decode()
        feedback = [data for data in feedback.split('\r\n\r\n') if data]
        for pack in feedback:
            self.now_msg.de_code(pack)
            if self.now_msg.sender == 'register':
                print('注册结果:', self.now_msg.content)
                if self.now_msg.content != 'True':
                    return False
        return True

    def send(self, receiver, msg):
        self.client_socket.send(self.now_msg.en_code(self.id, receiver, msg))

    def receive(self):
        feedback = self.client_socket.recv(1024).decode()
        feedback = [data for data in feedback.split('\r\n\r\n') if data]
        for pack in feedback:
            self.now_msg.de_code(pack)
            if self.now_msg.sender == 'friends':
                print('收到在线人员信息')
                self.friends = [data for data in self.now_msg.content.split('\r') if data]
                continue
            if self.now_msg.sender not in cmd and self.now_msg.receiver == self.id:
                print('{}收到{}消息:{}'.format(message.get_time_string(),
                                               self.now_msg.sender, self.now_msg.content))

    def close(self):
        self.send('offline', self.id)
        self.client_socket.close()

    def get_friends(self):
        try:
            while True:
                self.send('friends', self.pwd)
                feedback = self.client_socket.recv(1024).decode()
                feedback = [data for data in feedback.split('\r\n\r\n') if data]
                for pack in feedback:
                    self.now_msg.de_code(pack)
                    if self.now_msg.sender == 'friends':
                        self.friends = [data for data in self.now_msg.content.split('\r') if data]
                    else:
                        self.now_msg.de_code(pack)
                        if self.now_msg.sender not in cmd and self.now_msg.receiver == self.id:
                            print('{}收到{}消息:{}'.format(message.get_time_string(),
                                                           self.now_msg.sender, self.now_msg.content))
                # print(self.friends)
                time.sleep(1)
        except Exception as e:
            print("Error:", e)
        finally:
            exit(-1)

    def test_send(self):
        try:
            while True:
                self.send('0', self.id)
                time.sleep(1)
        except Exception as e:
            print('Error:', e)
        finally:
            exit(-3)


if __name__ == '__main__':
    client = Client('192.168.86.115', 8989)
    have_login = False
    while True:
        if not have_login:
            have_login = client.login('1', 'password')
        elif client.id == '0':
            print('欢迎进入管理员帐号')
        else:
            print('进入服务')
            threadPool = ThreadPoolExecutor(max_workers=4)
            threadPool.submit(client.get_friends)
            threadPool.submit(client.receive)
            threadPool.submit(client.test_send)
            threadPool.shutdown(wait=True)
        time.sleep(0.1)
