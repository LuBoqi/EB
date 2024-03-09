import sys
from multiprocessing import Process

from chat import Ui_Form2
from log import Ui_Form
from sign_up import Ui_Form3
import re
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
import threading
from concurrent.futures import ThreadPoolExecutor
from client import Client
import message
import time
import database
from server import cmd

server_ip = '127.0.0.1'
port = 8989


class Login(QtWidgets.QMainWindow, Ui_Form):
    ui1 = ''
    ui2 = ''

    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.Client = Client(server_ip, port)

    def login(self):
        box = QtWidgets.QMessageBox()
        user_name = self.lineEdit_3.text()  # 用户名
        password = self.lineEdit.text()  # 密码
        print(user_name, password)
        #   判断用户名和密码是否存在或正确
        if user_name == '' or password == '':
            box.warning(self, '错误', "用户名或密码不能为空")
        elif self.Client.login(user_name, password):
            self.ui1 = Chat(self.Client)
            self.ui1_refresh = Worker(self.ui1.ui_refresh)
            self.ui1.show()
            self.ui1_refresh.start()
            self.close()
        else:
            self.lineEdit.clear()
            box.warning(self, '错误', "用户名或密码错误")

    def sign_up(self):
        self.ui2 = Signup()
        self.ui2.show()

    def exit(self):
        self.close()
        self.Client.close()


class Worker(QThread):
    def __init__(self, func):
        super().__init__()
        self.func = func

    def run(self):
        self.func()


class Chat(QtWidgets.QMainWindow, Ui_Form2):
    # write chat code

    def run(self):
        self.ui_refresh()

    def __init__(self, client):
        super(Chat, self).__init__()
        self.setupUi(self)
        self.load_massage()
        self.Client = client
        self.recv_massage = Worker(self.Client.receive)
        self.get_friends = Worker(self.Client.get_friends)
        self.recv_massage.start()
        self.get_friends.start()
        self.new_info()

    def load_massage(self):
        # 加载数据库
        #     list
        # try:
        # for i in range(10):
        #     self.textBrowser.append(list[i,0] +'('+str(list[i,3])+')'+ ':' + list[i,2])
        # expect:
        #     box.warning(self, '提示', '更新失败')
        #     self.close() 更新错误可直接关掉
        pass

    def new_info(self):
        # 更新在线人列表
        list_f = []  # 好友列表
        list_n = self.Client.friends  # 在线列表
        self.listWidget.clear()
        for i in list_n:
            self.listWidget.addItem(i)

        # write code here

        pass

    def ui_refresh(self):
        last_time = message.get_time_string()
        while True:
            if self.Client.now_msg.time != last_time and self.Client.now_msg.sender not in cmd:
                self.textBrowser.append(
                    self.Client.now_msg.sender + '(' + self.Client.now_msg.time + ')' + ':' + self.Client.now_msg.content)
                last_time = self.Client.now_msg.time

    def send_massage(self):
        try:
            req = self.textEdit.toPlainText()
            if req:
                Time = time.strftime("%H:%M:%S", time.localtime())
                reqs = '我 ' + '(' + str(Time) + ')' + ':' + req
                self.textBrowser.append(reqs)
                self.Client.send(0, req)
                self.textEdit.clear()
                # 发送消息代码 write here
        #         写入数据库聊天记录代码 write here

        except Exception as e:
            print(e)


class Signup(QtWidgets.QMainWindow, Ui_Form3):
    def __init__(self):
        super(Signup, self).__init__()
        self.setupUi(self)
        self.client = Client(server_ip, port)

    def signup(self):
        try:
            box = QtWidgets.QMessageBox()
            nick_name = self.lineEdit.text()
            user_name = self.lineEdit_2.text()
            password = self.lineEdit_3.text()
            if len(nick_name) > 7:
                box.warning(self, '提示', '昵称太长')
            elif len(nick_name) == 0:
                box.warning(self, '提示', '昵称为空')
            elif len(user_name) > 8:
                box.warning(self, '提示', '账号太长')
            elif len(user_name) == 0:
                box.warning(self, '提示', '请输入账号')
            # elif type(user_name)=='str':
            #     box.warning(self, '提示', '账号不能有字母')
            elif len(password) > 12:
                box.warning(self, '提示', '密码太长')
            elif len(password) == 0:
                box.warning(self, '提示', '请输入密码')
            elif not re.match("^[a-zA-Z0-9_]{0,12}$", password):
                box.warning(self, "提示", "密码输入格式有误!")
            else:
                user = dict()
                # 需添加密码写入code    password=？？？
                user['nick_name'] = nick_name
                user['user_name'] = user_name
                user['password'] = password
                print(user)
                if self.client.register(user['user_name'], user['nick_name'], user['password']):
                    self.close()
                else:
                    box.warning(self, "提示", "账号已存在")
        except:
            box.warning(self, '提示', '注册失败')

    def exit(self):
        self.close()
