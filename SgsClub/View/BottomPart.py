import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

from View.BottomButton import BottomButton


class BottomPart(QWidget):
    homeSignal = pyqtSignal()
    meSignal = pyqtSignal()
    def __init__(self, parent = None):
        super().__init__(parent)

        #self.loadDataThread = LoadHomeDataThread()

        styleFile = QFile("../data/style/bottom.css")
        if styleFile.open(QIODevice.ReadOnly):
            stream = QTextStream(styleFile)
            self.setStyleSheet(stream.readAll())

        bgWgt = QWidget()
        bgWgt.setObjectName('bottomWgt')
        hrLayout = QHBoxLayout(self)
        hrLayout.setContentsMargins(0, 0, 0, 0)
        hrLayout.addWidget(bgWgt)

        self.homeBtn = BottomButton()
        homeIcon = QIcon(r'..\data\images\bottom\home_n.png')
        homeIcon.addFile(r'..\data\images\bottom\home_s.png', QSize(40, 40), QIcon.Active, QIcon.On)
        self.homeBtn.setIcon(homeIcon)
        self.homeBtn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.homeBtn.setText("首页")

        self.msgBtn = BottomButton()
        msgIcon = QIcon(r'..\data\images\bottom\msg_n.png')
        msgIcon.addFile(r'..\data\images\bottom\msg_s.png', QSize(40, 40), QIcon.Active, QIcon.On)
        self.msgBtn.setIcon(msgIcon)
        self.msgBtn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.msgBtn.setText("消息")

        self.postBtn = QPushButton()
        self.postBtn.setFixedSize(50, 50)
        self.postBtn.setObjectName('postBtn')

        self.searchBtn = BottomButton()
        searchIcon = QIcon(r'..\data\images\bottom\search_n.png')
        searchIcon.addFile(r'..\data\images\bottom\search_s.png', QSize(40, 40), QIcon.Active, QIcon.On)
        self.searchBtn.setIcon(searchIcon)
        self.searchBtn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.searchBtn.setText("搜索")

        self.meBtn = BottomButton()
        meIcon = QIcon(r'..\data\images\bottom\me_n.png')
        meIcon.addFile(r'..\data\images\bottom\me_s.png', QSize(40, 40), QIcon.Active, QIcon.On)
        self.meBtn.setIcon(meIcon)
        self.meBtn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.meBtn.setText("我")

        hrLayout = QHBoxLayout(bgWgt)
        hrLayout.setContentsMargins(10, 0, 10, 0)
        hrLayout.addWidget(self.homeBtn)
        hrLayout.addStretch()
        hrLayout.addWidget(self.msgBtn)
        hrLayout.addStretch()
        hrLayout.addWidget(self.postBtn)
        hrLayout.addStretch()
        hrLayout.addWidget(self.searchBtn)
        hrLayout.addStretch()
        hrLayout.addWidget(self.meBtn)

        self.homeBtn.clicked.connect(self.homeBtnClicked)
        self.meBtn.clicked.connect(self.meBtnClicked)

    def homeBtnClicked(self):
        self.homeSignal.emit()

    def meBtnClicked(self):
        self.meSignal.emit()

    def setHomeSelected(self):
        self.homeBtn.animateClick()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWgt = BottomPart()
    mainWgt.show()
    sys.exit(app.exec_())