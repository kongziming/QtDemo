import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from GetPostThread import GetPostThread


class ThreadTestUI(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.initUI()
        self.testThread = GetPostThread()

        #建立信号槽连接
        self.startBtn.clicked.connect(self.startBtnClicked)
        self.stopBtn.clicked.connect(self.stopBtnClicked)
        self.testThread.finished.connect(self.threadFinished)
        self.testThread.postSignal.connect(self.getPostSlot)

    def initUI(self):
        self.setWindowTitle('QThread Study')

        keywordLbl = QLabel('关键字(以逗号,隔开):')
        self.keywordEdit = QLineEdit()
        hrLayout = QHBoxLayout()
        hrLayout.addWidget(keywordLbl)
        hrLayout.addWidget(self.keywordEdit)

        resultLbl = QLabel('搜索结果:')
        self.resultList = QListWidget()
        vrLayout = QVBoxLayout()
        vrLayout.addWidget(resultLbl)
        vrLayout.addWidget(self.resultList)

        self.searchProgBar = QProgressBar()
        self.searchProgBar.setValue(0)
        self.stopBtn = QPushButton('停止')
        self.stopBtn.setEnabled(False)
        self.startBtn = QPushButton('开始')
        hrLayout1 = QHBoxLayout()
        hrLayout1.addWidget(self.stopBtn)
        hrLayout1.addWidget(self.startBtn)

        vrLayout1 = QVBoxLayout(self)
        vrLayout1.addLayout(hrLayout)
        vrLayout1.addLayout(vrLayout)
        vrLayout1.addWidget(self.searchProgBar)
        vrLayout1.addLayout(hrLayout1)

    def startBtnClicked(self):
        subreddit_list = str(self.keywordEdit.text()).split(',')
        if subreddit_list == ['']:
            print('没有搜索内容')
            return
        self.resultList.clear()
        count = len(subreddit_list)
        self.searchProgBar.setMaximum(count)
        self.testThread.setSubReddit(subreddit_list)
        self.testThread.start()
        self.startBtn.setEnabled(False)
        self.stopBtn.setEnabled(True)

    def stopBtnClicked(self):
        self.testThread.terminate()

    def threadFinished(self):
        self.stopBtn.setEnabled(False)
        self.startBtn.setEnabled(True)
        self.searchProgBar.setValue(0)
        print('获取结束')

    def getPostSlot(self, top_post):
        print(top_post)
        self.resultList.addItem(top_post)
        self.searchProgBar.setValue(self.searchProgBar.value() + 1)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    threadTestUi = ThreadTestUI()
    threadTestUi.show()
    sys.exit(app.exec_())