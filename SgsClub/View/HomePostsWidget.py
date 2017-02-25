#首页帖子

import sys
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtWidgets import *
from PyQt5.QtWebKitWidgets import *

class HomePostsWidget(QWidget):
    beginHtml = '''
        <!DOCTYPE html>
        <html>
        <head>
        <script>
        function getLink(obj)
        {
            pyObj.getLinkSlot(obj.children[0].innerHTML);
        }
        </script>
        </head>
        <body>
        <div id='bg'>
        '''
    endHtml = '''
        </div>
        </body>
        </html>
    '''
    postLinkSignal = pyqtSignal(str)
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setStyleSheet("background:transparent;")
        bgWgt = QWidget()
        hrLayout = QHBoxLayout(self)
        hrLayout.setContentsMargins(0, 0, 0, 0)
        hrLayout.addWidget(bgWgt)

        self.webView = QWebView()
        self.webView.settings().setAttribute(QWebSettings.AutoLoadImages, True)
        self.webView.settings().setAttribute(QWebSettings.LocalContentCanAccessRemoteUrls, True)
        self.webView.settings().setAttribute(QWebSettings.LocalContentCanAccessFileUrls, True)
        self.webView.settings().setAttribute(QWebSettings.LocalStorageDatabaseEnabled, True)
        self.webView.settings().setUserStyleSheetUrl(QUrl.fromLocalFile(os.getcwd()+'/css/homeposts.css'))
        self.webView.loadFinished.connect(self.htmlLoadFinished)

        vrLayout = QVBoxLayout(bgWgt)
        vrLayout.setContentsMargins(0, 0, 0, 0)
        vrLayout.addWidget(self.webView)

        html = '''
        <!DOCTYPE html>
        <html>
        <head>
        <script>
        function getLink(obj)
        {
            pyObj.getLinkSlot(obj.children[0].innerHTML);
        }
        </script>
        </head>
        <body>
        <div id='bg'>
        <div class='post'>
        <div class='top' style="font-weight: bold;color: #3C9D40;">社区活动，三国杀拜师堂</div>
        </div>
        <div class='post' onclick='getLink(this)'>
        <div class='link' style="display:none">dewdfew</div>
        <div class='title'>严白虎的寄篱有个问题哎</div>
        <div class='author'>post by <span>恋恋风尘<span></div>
        <div class='content'>邓艾濒死，使用红色的酒自救。他与我的距离为1，我发动寄篱，那么问题来了
        我既然成为了酒的目标，为什么我也恢复1体力，而不是令杀的伤害加一的效果？请详...</div>
        </div>
        <div class='post'>
        <div class='title'>严白虎的寄篱有个问题哎</div>
        <div class='author'>post by <span>恋恋风尘<span></div>
        <div class='content'>邓艾濒死，使用红色的酒自救。他与我的距离为1，我发动寄篱，那么问题来了
        我既然成为了酒的目标，为什么我也恢复1体力，而不是令杀的伤害加一的效果？请详...</div>
        </div>
        <div class='post'>
        <div class='title'>严白虎的寄篱有个问题哎</div>
        <div class='author'>post by <span>恋恋风尘<span></div>
        <div class='content'>邓艾濒死，使用红色的酒自救。他与我的距离为1，我发动寄篱，那么问题来了
        我既然成为了酒的目标，为什么我也恢复1体力，而不是令杀的伤害加一的效果？请详...</div>
        </div>
        <div class='post'>
        <div class='title'>严白虎的寄篱有个问题哎</div>
        <div class='author'>post by <span>恋恋风尘<span></div>
        <div class='content'>邓艾濒死，使用红色的酒自救。他与我的距离为1，我发动寄篱，那么问题来了
        我既然成为了酒的目标，为什么我也恢复1体力，而不是令杀的伤害加一的效果？请详...</div>
        </div>
        <div class='post'>
        <div class='title'>严白虎的寄篱有个问题哎</div>
        <div class='author'>post by <span>恋恋风尘<span></div>
        <div class='content'>邓艾濒死，使用红色的酒自救。他与我的距离为1，我发动寄篱，那么问题来了
        我既然成为了酒的目标，为什么我也恢复1体力，而不是令杀的伤害加一的效果？请详...</div>
        </div>
        <div class='post'>
        <div class='title'>严白虎的寄篱有个问题哎</div>
        <div class='author'>post by <span>恋恋风尘<span></div>
        <div class='content'>邓艾濒死，使用红色的酒自救。他与我的距离为1，我发动寄篱，那么问题来了
        我既然成为了酒的目标，为什么我也恢复1体力，而不是令杀的伤害加一的效果？请详...</div>
        </div>
        </div>
        </body>
        </html>
        '''
        self.webView.setHtml(html)

    def htmlLoadFinished(self, ready):
        if not ready:
            return
        self.webView.page().mainFrame().addToJavaScriptWindowObject("pyObj", self)

    #刷新数据（外部接口）
    def refreshContent(self, topList, downList):
        html = self.beginHtml
        for topPost in topList:
            newHtml = '''
                <div class='post' onclick='getLink(this)'>
                <div class='link' style="display:none">{0}</div>
                <div class='top' style="{1}">{2}</div>
                </div>'''.format(topPost['link'], topPost['style'], topPost['title'])
            html += newHtml
        for downPost in downList:
            newHtml = '''
                <div class='post' onclick='getLink(this)'>
                <div class='link' style="display:none">{0}</div>
                <div class='title'>{1}</div>
                <div class='author'>post by <span>{2}<span></div>
                <div class='content'>{3}</div>
                </div>
                '''.format(downPost['link'], downPost['title'], downPost['author'], downPost['summary'])
            html += newHtml
        html += self.endHtml
        self.webView.setHtml(html)

    @QtCore.pyqtSlot(str)
    def getLinkSlot(self, link):
        self.postLinkSignal.emit(link)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWgt = HomePostsWidget()
    mainWgt.show()
    sys.exit(app.exec_())