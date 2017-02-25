import sys
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtWidgets import *
from PyQt5.QtWebKitWidgets import *

class ReplyPostWidget(QWidget):
    commentSignal = pyqtSignal(str)
    def __init__(self, parent = None):
        super().__init__(parent)
        bgWgt = QWidget()
        bgWgt.setObjectName('bgWgt')
        hrLayout = QHBoxLayout(self)
        hrLayout.setContentsMargins(0, 0, 0, 0)
        hrLayout.addWidget(bgWgt)

        styleFile = QFile("../data/style/reply.css")
        if styleFile.open(QIODevice.ReadOnly):
            stream = QTextStream(styleFile)
            self.setStyleSheet(stream.readAll())

        self.commentEdit = QLineEdit()
        self.commentEdit.setObjectName('commentEdit')
        self.commentEdit.setMinimumHeight(26)
        self.commentEdit.setPlaceholderText('写回复...')
        self.commentBtn = QPushButton()
        self.commentBtn.setObjectName('commentBtn')
        self.commentBtn.setText('发 送')
        self.commentBtn.setFixedSize(46, 26)
        hrLayout1 = QHBoxLayout(bgWgt)
        hrLayout1.setContentsMargins(5, 5, 5, 5)
        hrLayout1.setSpacing(5)
        hrLayout1.addWidget(self.commentEdit)
        hrLayout1.addWidget(self.commentBtn)

        self.commentBtn.clicked.connect(self.onCommentBtnClicked)

    def onCommentBtnClicked(self):
        comment = self.commentEdit.text()
        self.commentSignal.emit(comment)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWgt = ReplyPostWidget()
    mainWgt.show()
    sys.exit(app.exec_())
