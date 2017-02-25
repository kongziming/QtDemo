import requests
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from bs4 import BeautifulSoup

agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.8 Mobile Safari/537.36'
baseUrl = "http://club.sanguosha.com/forum.php?mod=viewthread&tid=206633&page=1&mobile=2"
headers = {
    'Connection':'keep-alive',
    'Host': 'club.sanguosha.com',
    'User-Agent': agent,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'
}

r = requests.get(baseUrl, headers=headers)

msgList = []

soup = BeautifulSoup(r.text, 'lxml')

for replyContent in soup.find_all(class_='plc cl'):
    if replyContent.find(class_='display pi'):
        reply = {}
        reply['avatar'] = replyContent.find(class_='avatar')
        reply['author']=replyContent.find(class_='blue').get_text()
        reply['message']=replyContent.find(class_='message')
        msgList.append(reply)
        print(reply)

