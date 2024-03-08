import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
import log


if __name__ == "__main__":
        app = QApplication(sys.argv)
        # ui = log.Ui_Form()
        mainWindow = QMainWindow()
        ui2 = log.Ui_Form()
        # 调用Ui_MainWindow类的setupUi，创建初始组件
        ui2.setupUi(mainWindow)
        mainWindow.show()
        # 进入程序的主循环，并通过exit函数确保主循环安全结束
        sys.exit(app.exec_())