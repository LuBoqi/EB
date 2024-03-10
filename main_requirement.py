from multiprocessing import Process
from chat import Ui_Form2
from log import Ui_Form
from sign_up import Ui_Form3
import re
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from client import Client
import message
import time
from server import cmd
from database import ChatLogs

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
            self.ui1.show()
            self.close()
            self.ui1.go()
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

    def go(self):
        self.rec = Worker(self.receive)
        # self.rec = Process(target=self.Client.receive)
        # self.fri = Worker(self.Client.get_friends)
        # self.fri = Process(target=self.Client.get_friends)
        self.uiRefresh = Worker(self.ui_refresh)
        # self.uiRefresh = Process(target=self.ui_refresh)
        self.rec.start()
        # self.fri.start()
        self.uiRefresh.start()
        # self.rec.start()
        # self.fri.start()
        # self.uiRefresh.start()

    def __init__(self, client):
        super(Chat, self).__init__()
        self.setupUi(self)
        # self.load_massage()
        self.chatlogs = ChatLogs('chat_logs.csv')
        self.Client = client
        # self.recv_massage = Worker(self.Client.receive)
        # self.get_friends = Worker(self.Client.get_friends)
        # self.recv_massage.start()
        # self.get_friends.start()
        self.load_massage()
        self.new_info()

    def clear_massage(self):
        self.textBrowser.clear()

    def load_massage(self):
        box = QtWidgets.QMessageBox()
        # 加载数据库
        user_id = self.Client.id
        list= self.chatlogs.get_messages(user_id,user_id)
        try:
            for i in range(10):
                self.textBrowser.append(str(list[i][0]) + '(' + str(list[i][3]) + ')' + ':' + str(list[i][2]))
        except:
            box.warning(self, '提示', '更新失败')


    def new_info(self):
        self.listWidget.clear()
        for i in self.Client.friends:
            self.listWidget.addItem(i)

    def ui_refresh(self):
        last_time = message.get_time_string()
        while True:
            if self.Client.now_msg.time != last_time and self.Client.now_msg.sender not in cmd:
                self.textBrowser.append(
                    self.Client.now_msg.sender + '(' + self.Client.now_msg.time + ')' + ':' + self.Client.now_msg.content)


                last_time = self.Client.now_msg.time

    def receive(self):
        while True:
            self.Client.receive()
            if self.Client.now_msg.sender == 'friends':
                self.new_info()


    def send_massage(self):
        try:
            req = self.textEdit.toPlainText()
            s = re.findall(r"\W", req)
            if s != []:
                sym1 = re.findall(r"\W", req)[0]
                sym2 = re.findall(r"\W", req)[1]
            else:
                sym1 = 0
                sym2 = 0
            Time = time.strftime("%H:%M:%S", time.localtime())
            if sym1 == '@' and (sym2==':' or sym2 == '：'):
                # sendto =
                if sym2==':':
                    p = re.compile(r'[@](.*?)[:]', re.S)
                    sendto = re.findall(p, req)[0]
                    reqq= '(私聊)'+req.split(':',1)[1]
                    reqs = '我 ' + '(私聊'+ str(sendto) +')' +'(' + str(Time) + ')' + ':' + req.split('：', 1)[1]
                elif sym2=="：":
                    p = re.compile(r'[@](.*?)[：]', re.S)
                    sendto = re.findall(p, req)[0]
                    reqq = '(私聊)'+ req.split('：', 1)[1]
                    reqs = '我 ' + '(私聊'+ str(sendto) +')' +'(' + str(Time) + ')' + ':' + req.split('：', 1)[1]
            else:
                sendto = 0
                reqq=req
                reqs = '我 ' + '(' + str(Time) + ')' + ':' + reqq

            # if req:
            #     Time = time.strftime("%H:%M:%S", time.localtime())
            #     reqs = '我 ' + '(' + str(Time) + ')' + ':' + req
            self.textBrowser.append(reqs)
            self.Client.send(sendto, reqq)
            self.textEdit.clear()

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
