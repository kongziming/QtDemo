import json
import sys
import time
import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class ThreadTestUI(QWidget):
    agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.8 Safari/537.36'
    headers = {
        'User-Agent': agent
    }

    def __init__(self, parent = None):
        super().__init__(parent)
        self.initUI()
        #建立信号槽连接
        self.startBtn.clicked.connect(self.startBtnClicked)

    def initUI(self):
        #初始化界面控件
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
        for post in self.get_top_from_subreddits(subreddit_list):
            self.resultList.addItem(post)


    def get_top_post(self,subreddit):
        #从服务器获取数据
        url = "https://www.reddit.com/r/{}.json?limit=1".format(subreddit)
        try:
            restext = requests.get(url, headers=self.headers)
            data = json.loads(restext.text)
            top_post = data['data']['children'][0]['data']
        except Exception as e:
            print(e)
            return '错误数据'
        return "'{title}' by {author} in {subreddit}".format(**top_post)

    def get_top_from_subreddits(self,subreddits):
        for subreddit in subreddits:
            yield self.get_top_post(subreddit)
            time.sleep(2)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    threadTestUi = ThreadTestUI()
    threadTestUi.show()
    sys.exit(app.exec_())