import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class LoginWidget(QWidget):
    loginSignal = pyqtSignal(str, str)
    def __init__(self, parent = None):
        super().__init__(parent)

        bgWgt = QWidget()
        hrLayout = QHBoxLayout(self)
        hrLayout.setContentsMargins(0, 0, 0, 0)
        hrLayout.addWidget(bgWgt)
        bgWgt.setObjectName('bgWgt')

        styleFile = QFile("../data/style/login.css")
        if styleFile.open(QIODevice.ReadOnly):
            stream = QTextStream(styleFile)
            self.setStyleSheet(stream.readAll())

        hrLayout1 = QHBoxLayout()
        logoLbl = QLabel()
        logoLbl.setFixedSize(210, 130)
        logoLbl.setObjectName('logoLbl')
        hrLayout1.addStretch()
        hrLayout1.addWidget(logoLbl)
        hrLayout1.addStretch()

        self.userNameEdit = QLineEdit()
        self.pwdEdit = QLineEdit()
        self.loginBtn = QPushButton()
        self.userNameEdit.setObjectName('userNameEdit')
        self.pwdEdit.setObjectName('pwdEdit')
        self.loginBtn.setObjectName('loginBtn')
        self.loginBtn.setMinimumHeight(26)
        self.pwdEdit.setEchoMode(QLineEdit.Password)
        self.userNameEdit.setPlaceholderText('用户名')
        self.pwdEdit.setPlaceholderText('密码')
        self.loginBtn.setText('登录')
        vrLayout = QVBoxLayout(bgWgt)
        vrLayout.setSpacing(30)
        vrLayout.addStretch()
        vrLayout.addLayout(hrLayout1)
        vrLayout.addWidget(self.userNameEdit)
        vrLayout.addWidget(self.pwdEdit)
        vrLayout.addWidget(self.loginBtn)
        vrLayout.addStretch()

        self.loginBtn.clicked.connect(self.loginBtnClicked)

    #登录按钮单击
    def loginBtnClicked(self):
        self.loginSignal.emit(self.userNameEdit.text(), self.pwdEdit.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWgt = LoginWidget()
    mainWgt.show()
    sys.exit(app.exec_())