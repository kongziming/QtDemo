from PyQt5.QtCore import QThread
from bs4 import BeautifulSoup
from PyQt5.QtCore import pyqtSignal

class HomePageThread(QThread):
    postDataSignal = pyqtSignal(list, list)
    agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.8 Mobile Safari/537.36'
    baseUrl = "http://club.sanguosha.com/"
    headers = {
        'Connection':'keep-alive',
        'Host': 'club.sanguosha.com',
        'User-Agent': agent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'
    }


    def __init__(self, parent=None):
        super().__init__(parent)
        import requests
        self.rt = requests.session()

    def __del__(self):
        self.wait()

    def run(self):
        topList = []    #置顶帖子
        downList = []   #未指定帖子
        r = self.rt.get(self.baseUrl, headers=self.headers)
        soup = BeautifulSoup(r.text, 'lxml')

        #获取置顶帖子内容
        for post in soup.find_all(class_='tl_top'):
            titleSoup = post.find('a')
            if titleSoup:
                topPost = {}
                topPost['link'] = titleSoup['href']
                topPost['style'] = titleSoup['style']
                topPost['title'] = titleSoup.string.strip()
                topList.append(topPost)

        #获取未置顶帖子
        for post in soup.find_all(class_='tl_shadow'):
            titleSoup = post.find('a')
            if titleSoup:
                downPost = {}
                downPost['link'] = post.find(class_='ti_item')['href']
                downPost['author'] = post.find(class_='ti_author').text
                downPost['title'] = post.find(class_='ti_title').text.strip()
                downPost['summary'] = post.find(class_='ti_abs').text
                downPost['time'] = post.find(class_='ti_time').text
                downPost['replynum'] = post.find(class_='btn_icon').text
                downList.append(downPost)

        self.postDataSignal.emit(topList, downList)