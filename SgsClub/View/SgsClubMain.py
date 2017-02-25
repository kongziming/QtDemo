#主界面

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from View.ResizableWidget import ResizableWidget
from View.BottomPart import BottomPart
from View.HomeTop import HomeTop
from View.HomePostsWidget import HomePostsWidget
from View.SinglePostWidget import SinglePostWidget
from View.LoginWidget import LoginWidget
from Control.HomePageThread import HomePageThread
from Control.PostPageThread import PostPageThread
from Control.SgsClub import SgsClub

class SgsClubMain(ResizableWidget):
    def __init__(self, parent=None):
        #初始化
        super().__init__(parent)
        hrLayout = QHBoxLayout(self)
        hrLayout.setContentsMargins(0, 0, 0, 0)
        bgWgt = QWidget()
        bgWgt.setObjectName('clubMain')
        hrLayout.addWidget(bgWgt)

        #是否已登录
        self.isLogin = False

        #加载样式表
        styleFile = QFile("../data/style/main.css")
        if styleFile.open(QIODevice.ReadOnly):
            stream = QTextStream(styleFile)
            self.setStyleSheet(stream.readAll())

        #stackedWidget
        homeWgt = QWidget()#首页，第0页
        #self.postWgt = SinglePostWgt()


        #首页
        homeTop = HomeTop()
        self.postsWgt = HomePostsWidget()#首页帖子widget
        vrLayout1 = QVBoxLayout(homeWgt)
        vrLayout1.setContentsMargins(0, 0, 0, 0)
        vrLayout1.addWidget(homeTop)
        vrLayout1.addWidget(self.postsWgt)

        #单个帖子
        self.postWgt = SinglePostWidget()

        #登录
        self.loginWgt = LoginWidget()

        self.stackedWgt = QStackedWidget()
        self.stackedWgt.addWidget(homeWgt)
        self.stackedWgt.addWidget(self.postWgt)
        self.stackedWgt.addWidget(self.loginWgt)

        vrLayout = QVBoxLayout(bgWgt)
        vrLayout.setContentsMargins(0, 0, 0, 0)
        self.bottomPart = BottomPart()
        vrLayout.addWidget(self.stackedWgt)
        vrLayout.addWidget(self.bottomPart)

        self.resize(370, 600)

        #加载数据的线程
        self.loadHomePageThread = HomePageThread()#首页
        self.loadPostPageThread = PostPageThread()#帖子

        #信号槽连接
        self.bottomPart.homeSignal.connect(self.homeBtnClicked)
        self.loadHomePageThread.postDataSignal.connect(self.refreshHomePageSlot)
        self.postsWgt.postLinkSignal.connect(self.openPostSlot)
        self.loadPostPageThread.postDataSignal.connect(self.loadPostData)
        self.postWgt.homeSignal.connect(self.returnToHome)
        self.bottomPart.meSignal.connect(self.meBtnClicked)
        self.loginWgt.loginSignal.connect(self.loginClubSlot)
        self.postWgt.replySignal.connect(self.replyToPost)

        #登录、发帖、回帖
        self.sgsClub = SgsClub()


    #首页按钮单击，刷新首页内容
    def homeBtnClicked(self):
        if self.stackedWgt.currentIndex() != 0:
            self.stackedWgt.setCurrentIndex(0)
            return
        self.loadHomePageThread.terminate()
        self.loadHomePageThread.start()

    #刷新首页数据线程完成槽函数
    def refreshHomePageSlot(self, topList, downList):
        self.loadHomePageThread.terminate()
        self.postsWgt.refreshContent(topList, downList)
        #print(topList)
        #print(downList)

    #点击帖子，打开帖子，加载数据
    def openPostSlot(self, link):
        self.loadPostPageThread.terminate()
        self.loadPostPageThread.setPostLink(link)
        self.loadPostPageThread.start()


    #加载帖子线程完成槽函数
    def loadPostData(self, postid, postData):
        self.loadPostPageThread.terminate()
        self.stackedWgt.setCurrentIndex(1)
        self.bottomPart.hide()
        self.postWgt.setPostId(postid)
        self.postWgt.setPostContent(postData)

    #回到首页槽函数
    def returnToHome(self):
        self.stackedWgt.setCurrentIndex(0)
        self.bottomPart.show()
        print('回到首页了')

    def meBtnClicked(self):
        if not self.isLogin:
            self.stackedWgt.setCurrentIndex(2)

    def loginClubSlot(self, usrName, pwd):
        print(usrName)
        print(pwd)
        self.sgsClub.loginClub(usrName, pwd)
        self.sgsClub.setFormhash()
        self.isLogin = True
        #self.stackedWgt.setCurrentIndex(0)
        self.bottomPart.setHomeSelected()

    def replyToPost(self, postid, content):
        print(postid)
        print(content)
        self.sgsClub.reply(59, postid, content)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWgt = SgsClubMain()
    mainWgt.show()
    sys.exit(app.exec_())