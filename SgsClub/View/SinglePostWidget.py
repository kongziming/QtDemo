import sys
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtWidgets import *
from PyQt5.QtWebKitWidgets import *
from View.ReplyPostWidget import ReplyPostWidget
from View.PostTopWidget import PostTopWidget

class SinglePostWidget(QWidget):
    beginHtml = '''
        <!DOCTYPE html>
        <html>
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        </head>
        <body>
        <div id='bg'>
        '''
    endHtml = '''
        </div>
        </body>
        </html>
    '''
    homeSignal = pyqtSignal()
    replySignal = pyqtSignal(str, str)
    def __init__(self, parent = None):
        super().__init__(parent)
        bgWgt = QWidget()
        hrLayout = QHBoxLayout(self)
        hrLayout.setContentsMargins(0, 0, 0, 0)
        hrLayout.addWidget(bgWgt)

        self.posttopWgt = PostTopWidget()
        self.webView = QWebView()
        self.webView.settings().setDefaultTextEncoding("GB2312")
        self.webView.settings().setUserStyleSheetUrl(QUrl.fromLocalFile(os.getcwd()+'/css/post.css'))
        self.commentWgt = ReplyPostWidget()
        vrLayout = QVBoxLayout(bgWgt)
        vrLayout.setContentsMargins(0, 0, 0, 0)
        vrLayout.setSpacing(0)
        vrLayout.addWidget(self.posttopWgt)
        vrLayout.addWidget(self.webView)
        vrLayout.addWidget(self.commentWgt)

        self.posttopWgt.homeSignal.connect(self.homeBtnClicked)
        self.commentWgt.commentSignal.connect(self.replyBtnClicked)

    def setPostId(self, postid):
        self.postid = postid


    #刷新数据（外部接口）
    def setPostContent(self, msgList):
        html = self.beginHtml
        for postContent in msgList:
            #print(postContent)
            content = str(postContent['message'])
            content = content.replace('src="','src="http://club.sanguosha.com/')
            newHtml  = '''<div class='reply'>
            <div class='left'><div class='avatar'><img src={0}/></div></div>
            <div class='right'><div class='author'>{1}</div>
            <div class='operate'></div>
            <div class='message'>{2}</div>
            </div>
            </div>
            '''.format(postContent['avatar'],postContent['author'],content)
            html += newHtml
        print('界面中帖子内容加载结束')
        html += self.endHtml
        #print(html)
        postfile = open(os.getcwd()+'/pages/post.html', 'w',encoding='utf-8')
        postfile.write(html)
        postfile.close()
        url = QUrl.fromLocalFile(os.getcwd()+'/pages/post.html')
        self.webView.load(url)

    #返回首页按钮单击
    def homeBtnClicked(self):
        print(1)
        self.homeSignal.emit()

    def replyBtnClicked(self, comment):
        self.replySignal.emit(self.postid, comment)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWgt = SinglePostWidget()
    mainWgt.show()
    sys.exit(app.exec_())