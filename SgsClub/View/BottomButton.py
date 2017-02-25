from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QToolButton
from qtpy import QtCore
from qtpy import QtGui

class BottomButton(QToolButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setAutoExclusive(True)
        self.setCheckable(True)
        self.setIconSize(QSize(35, 35))

    def enterEvent(self, QEvent):
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def leaveEvent(self, QEvent):
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))