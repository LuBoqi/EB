import main_requirement
import sys
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ui = log.Ui_Form()
    ui2 = main_requirement.Login()
    # 调用Ui_MainWindow类的setupUi，创建初始组件
    ui2.show()
    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())