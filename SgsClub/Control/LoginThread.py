from PyQt5.QtCore import QThread
from bs4 import BeautifulSoup
from PyQt5.QtCore import pyqtSignal

class LoginThread(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)

    def __del__(self):
        self.wait()

    def run(self):
        pass
