import json
import requests
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal


class GetPostThread(QThread):
    postSignal = pyqtSignal(str)

    agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.8 Safari/537.36'
    headers = {
        'User-Agent': agent
    }

    def __init__(self):
        QThread.__init__(self)
        self.subreddits = []

    def __del__(self):
        self.wait()

    def setSubReddit(self, subReddit):
        self.subreddits = subReddit

    def _get_top_post(self, subreddit):
        url = "https://www.reddit.com/r/{}.json?limit=1".format(subreddit)
        print(url)
        try:
            restext = requests.get(url, headers=self.headers)
            data = json.loads(restext.text)
            top_post = data['data']['children'][0]['data']
        except Exception as e:
            print(e)
            return '错误数据'
        return "'{title}' by {author} in {subreddit}".format(**top_post)

    def run(self):
        for subreddit in self.subreddits:
            top_post = self._get_top_post(subreddit)
            self.postSignal.emit(top_post)
            self.sleep(2)