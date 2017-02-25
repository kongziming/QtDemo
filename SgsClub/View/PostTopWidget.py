import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class PostTopWidget(QWidget):
    homeSignal = pyqtSignal()
    def __init__(self, parent = None):
        super().__init__(parent)

        bgWgt = QWidget()
        hrLayout = QHBoxLayout(self)
        hrLayout.setContentsMargins(0, 0, 0, 0)
        hrLayout.addWidget(bgWgt)
        bgWgt.setObjectName('posttopWgt')

        styleFile = QFile("../data/style/posttop.css")
        if styleFile.open(QIODevice.ReadOnly):
            stream = QTextStream(styleFile)
            self.setStyleSheet(stream.readAll())

        self.returnHome = QPushButton()
        self.returnHome.setObjectName('returnHome')
        self.returnHome.setFixedSize(19, 35)
        self.titleBtn = QPushButton()
        self.titleBtn.setObjectName('titleBtn')
        self.titleBtn.setText('帖子正文')
        self.tempBtn = QPushButton()
        self.tempBtn.setObjectName('tempBtn')
        self.tempBtn.setFixedSize(35, 35)

        hrLayout1 = QHBoxLayout(bgWgt)
        hrLayout1.setContentsMargins(10, 4, 10, 4)
        hrLayout1.addWidget(self.returnHome)
        hrLayout1.addStretch()
        hrLayout1.addWidget(self.titleBtn)
        hrLayout1.addStretch()
        hrLayout1.addWidget(self.tempBtn)

        self.returnHome.clicked.connect(self.returnHomeBtnClicked)

    def returnHomeBtnClicked(self):
        self.homeSignal.emit()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWgt = PostTopWidget()
    mainWgt.show()
    sys.exit(app.exec_())