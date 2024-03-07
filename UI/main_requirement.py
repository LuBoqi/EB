import sys
from chat import Ui_Form2
from log import Ui_Form
from sign_up import Ui_Form3

import re
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtWidgets, QtCore, QtGui, Qt
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import client
import socket

class Login(QtWidgets.QMainWindow,Ui_Form):
    ui1 = ''
    ui2 = ''
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)

    def login(self):
        box=QtWidgets.QMessageBox()
        user_name=self.lineEdit_3.text()  #用户名
        password=self.lineEdit.text()   #密码
    #   判断用户名和密码是否存在或正确
    #   write code here
    #   连接成功使用
    #   self.ui1 = Chat()
    #   self.ui1.show()
    #   self.close()

    def sign_up(self):
        self.ui2 = Signup()
        self.ui2.show()

    def exit(self):
        self.close()
        #需要客户端退出代码




class Chat(QtWidgets.QMainWindow,Ui_Form2):
    # write chat code
    pass

class Signup(QtWidgets.QMainWindow,Ui_Form3):
    def __init__(self):
        super(Signup, self).__init__()
        self.setupUi(self)

    def signup(self):
        try:
            box=QtWidgets.QMessageBox()
            nick_name=self.lineEdit.text()
            user_name=self.lineEdit_2.text()
            password=self.lineEdit_3.text()
            if len(nick_name) > 7:
                box.warning(self, '提示', '昵称太长')
            elif len(nick_name) == 0:
                box.warning(self, '提示', '昵称为空')
            elif len(user_name) > 8:
                box.warning(self, '提示', '账号太长')
            elif len(user_name) == 0:
                box.warning(self, '提示', '请输入账号')
            elif len(password) > 12:
                box.warning(self, '提示', '密码太长')
            elif len(password) == 0:
                box.warning(self, '提示', '请输入密码')
            elif not re.match("^[a-zA-Z0-9_]{0,12}$", password):
                box.warning(self, "提示", "密码输入格式有误!")
            else:
                user=dict()
                # 需添加密码写入code    password=？？？
                user['nick_name']=nick_name
                user['user_name']=user_name
                user['password']=password
                print(user)
        #   需添加写入注册代码

        except:
            box.warning(self, '提示', '注册失败')
    def exit(self):
        self.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    # ui = log.Ui_Form()
    ui2=Signup()
    # 调用Ui_MainWindow类的setupUi，创建初始组件
    ui2.show()
    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())
