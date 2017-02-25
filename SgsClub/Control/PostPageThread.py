import re
import requests
from PyQt5.QtCore import QThread
from bs4 import BeautifulSoup
from PyQt5.QtCore import pyqtSignal


class PostPageThread(QThread):
    postDataSignal = pyqtSignal(str,list)
    agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.8 Mobile Safari/537.36'
    baseUrl = "http://club.sanguosha.com/"
    postlink = baseUrl
    headers = {
        'Connection':'keep-alive',
        'Host': 'club.sanguosha.com',
        'User-Agent': agent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'
    }


    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        self.rt = requests.session()

    def __del__(self):
        self.wait()

    def getPostContent(self):
        msgList = []
        r = self.rt.get(self.postlink, headers=self.headers)
        #print(r.text)
        soup = BeautifulSoup(r.text, 'lxml')  #声明BeautifulSoup对象
        for replyContent in soup.find_all(class_='plc cl'):
            if replyContent.find(class_='display pi'):
                reply = {}
                reply['avatar'] = replyContent.find(class_='avatar').img['src']
                reply['author']=replyContent.find(class_='blue').get_text()
                reply['message']=replyContent.find(class_='message')
                msgList.append(reply)
                #print(reply)
        #print(22)
        self.postDataSignal.emit(self.postid,msgList)

    def run(self):
        self.getPostContent()

    #设置帖子链接
    def setPostLink(self, link):
        self.postlink = self.baseUrl + link.replace('amp;','')
        postrow = re.findall(r'tid=(.*?)&', link)
        if len(postrow) != 0:
            self.postid = postrow[0]
        print(self.postlink)
        print(self.postid)

if __name__ == '__main__':
    rr = PostPageThread()
    rr.start()