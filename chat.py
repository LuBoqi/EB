# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form2(object):
    def setupUi(self, Form2):
        Form2.setObjectName("Form2")
        Form2.resize(910, 642)
        Form2.setStyleSheet("background-image: url(:/background/whitebackground.jpg);\n"
"background-image: url(:/background/UI/whitebackground.jpg);")
        self.frame = QtWidgets.QFrame(Form2)
        self.frame.setGeometry(QtCore.QRect(90, 70, 711, 501))
        self.frame.setStyleSheet("background-image: url(:/background/whitebackground.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(20, 310, 471, 171))
        self.textEdit.setStyleSheet("background-image: url(:/background/UI/whitebackground.jpg);\n"
"font: 12pt \"华文楷体\";\n"
"background-image: url(:/background/UI/background3.jpg);")
        self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(20, 70, 471, 241))
        self.textBrowser.setStyleSheet("background-image: url(:/background/UI/background3.jpg);\n"
"font: 12pt \"华文楷体\";")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_2.setGeometry(QtCore.QRect(490, 70, 201, 41))
        self.textBrowser_2.setStyleSheet("background-image: url(:/background/UI/whitebackground.jpg);\n"
"background-image: url(:/background/UI/background3.jpg);")
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(19, 20, 671, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.frame_3.setPalette(palette)
        self.frame_3.setStyleSheet("background-image: url(:/background/UI/background3.jpg);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setMidLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.frame_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(280, 10, 71, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.textBrowser_3.setPalette(palette)
        self.textBrowser_3.setMouseTracking(True)
        self.textBrowser_3.setTabletTracking(False)
        self.textBrowser_3.setAcceptDrops(True)
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_3.setTabChangesFocus(False)
        self.textBrowser_3.setUndoRedoEnabled(False)
        self.textBrowser_3.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textBrowser_3.setOverwriteMode(False)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setGeometry(QtCore.QRect(610, 0, 31, 28))
        self.pushButton_5.setStyleSheet("background-image: url(:/background/UI/whitebackground.jpg);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_6.setGeometry(QtCore.QRect(640, 0, 31, 28))
        self.pushButton_6.setStyleSheet("background-image: url(:/background/UI/whitebackground.jpg);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(419, 440, 61, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(489, 109, 201, 371))
        self.listWidget.setStyleSheet("background-image: url(:/background/UI/whitebackground.jpg);\n"
"font: 75 12pt \"Agency FB\";\n"
"background-image: url(:/background/UI/background3.jpg);")
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(79, 440, 51, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 440, 51, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser_2.raise_()
        self.textBrowser.raise_()
        self.frame_3.raise_()
        self.textEdit.raise_()
        self.pushButton_4.raise_()
        self.listWidget.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(Form2)
        self.pushButton_6.clicked.connect(Form2.exit) # type: ignore
        self.pushButton_5.clicked.connect(Form2.showMinimized) # type: ignore
        self.pushButton_4.clicked.connect(Form2.send_massage) # type: ignore
        self.pushButton.clicked.connect(Form2.clear_massage) # type: ignore
        self.pushButton_2.clicked.connect(Form2.load_massage) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form2)

    def retranslateUi(self, Form2):
        _translate = QtCore.QCoreApplication.translate
        Form2.setWindowTitle(_translate("Form2", "Form"))
        self.textBrowser_2.setHtml(_translate("Form2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">在线人员</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Form2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">聊天室</span></p></body></html>"))
        self.pushButton_5.setText(_translate("Form2", "-"))
        self.pushButton_6.setText(_translate("Form2", "X"))
        self.pushButton_4.setText(_translate("Form2", "发送"))
        self.pushButton.setText(_translate("Form2", "清除"))
        self.pushButton_2.setText(_translate("Form2", "更新"))
import pictures_rc
