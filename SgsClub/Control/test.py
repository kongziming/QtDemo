import requests
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from bs4 import BeautifulSoup

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

r = requests.get(baseUrl, headers=headers)

topList = []    #置顶帖子
downList = []   #未指定帖子

#print(r.text)
soup = BeautifulSoup(r.text, 'lxml')
for post in soup.find_all(class_='tl_top'):
    titleSoup = post.find('a')
    if titleSoup:
        pass
        #print(titleSoup['href'])
        #print(titleSoup['style'])
        #print(titleSoup.string)

#获取未置顶帖子
for post in soup.find_all(class_='tl_shadow'):
    downPost = {}
    downPost['link'] = post.find('a')['href']
    downPost['author'] = post.find(class_='ti_author').text
    downPost['title'] = post.find(class_='ti_title').text.strip()
    downPost['summary'] = post.find(class_='ti_abs').text
    downList.append(downPost)

print(downList)