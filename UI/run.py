import sys
from chat import Ui_Form2
from log import Ui_Form

from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtWidgets, QtCore, QtGui, Qt
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import client
import socket

class Login(QtWidgets.QMainWindow,Ui_Form):
    # write login code
    pass

class Chat(QtWidgets.QMainWindow,Ui_Form2):
    # write chat code
    pass



if __name__ == '__main__':

    app = QApplication(sys.argv)

    # 创建对象
    mainWindow = QMainWindow()

    # ui = log.Ui_Form()
    ui2=Ui_Form()
    # 调用Ui_MainWindow类的setupUi，创建初始组件
    ui2.setupUi(mainWindow)
    # 创建窗口
    mainWindow.show()
    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())
