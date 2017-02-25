import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from qtpy import QtCore
from qtpy import QtGui

class ResizableWidget(QWidget):
    _resizable = True
    _marginWidth = 4
    _bPressed = False
    def __init__(self, parent = None):
        super().__init__(parent)
        #self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.setAttribute(Qt.WA_Hover)
        self.installEventFilter(self)

    def changeMouseStyle(self, point):
        if not self._resizable:
            self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self._mouseStyle = 0
            return

        iPosX = point.x()
        iPosY = point.y()

        iWidth = self.width()
        iHeight = self.height()
        if (iPosX >= iWidth - self._marginWidth and iPosX <= iWidth):
            self.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))#右
            if (iPosY >= iHeight - self._marginWidth and iPosY <= iHeight):
                self.setCursor(QtGui.QCursor(QtCore.Qt.SizeFDiagCursor))#右下
                self._mouseStyle = 5
                return
            self._mouseStyle = 4
            return

        if (iPosY >= iHeight - self._marginWidth and iPosY <= iHeight):
            self.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))#下
            self._mouseStyle = 6
            return

        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))#正常样式
        self._mouseStyle = 0;
        return

    def eventFilter(self, obj, event):
        #鼠标移动
        if event.type() == QtCore.QEvent.HoverMove:
            if not self._bPressed:
                self.changeMouseStyle(event.pos())
            else:
                ptGlobalPos = self.mapToGlobal(event.pos())
                ptTopLeft = self.frameGeometry().topLeft()
                ptBottomRight = self.frameGeometry().bottomRight()
                if self._mouseStyle == 0:
                    self.move(self.mapToGlobal(event.pos()) - self._ptPressPos)
                    return True
                elif self._mouseStyle == 4:
                    if (ptGlobalPos.x() - ptTopLeft.x() > self.minimumWidth()):
                        ptBottomRight.setX(ptGlobalPos.x())
                    else:
                        ptBottomRight.setX(ptTopLeft.x() + self.minimumWidth())
                elif self._mouseStyle == 6:
                    if (ptGlobalPos.y() - ptTopLeft.y() > self.minimumHeight()):
                        ptBottomRight.setY(ptGlobalPos.y())
                    else:
                        ptBottomRight.setY(ptTopLeft.y() + self.minimumHeight())
                elif self._mouseStyle == 5:
                    if (ptGlobalPos.x() - ptTopLeft.x() > self.minimumWidth()):
                        ptBottomRight.setX(ptGlobalPos.x())
                    else:
                        ptBottomRight.setX(ptTopLeft.x() + self.minimumWidth())
                    if (ptGlobalPos.y() - ptTopLeft.y() > self.minimumHeight()):
                        ptBottomRight.setY(ptGlobalPos.y())
                    else:
                        ptBottomRight.setY(ptTopLeft.y() + self.minimumHeight())
                self.setGeometry(QRect(ptTopLeft, ptBottomRight))

        #鼠标按下
        elif event.type() == QtCore.QEvent.MouseButtonPress:
            pressPt = event.pos()
            if (pressPt.y() <= 50 or self._mouseStyle != 0):
                self._bPressed = True
                self._ptPressPos = event.globalPos() - self.frameGeometry().topLeft()

        #鼠标松开
        elif event.type() == QtCore.QEvent.MouseButtonRelease:
            self._bPressed = False

        elif event.type() == QtCore.QEvent.ScrollPrepare:
            if(self._mouseStyle != 0):
                print(22)
                return False;
        return False


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWgt = ResizableWidget()
    mainWgt.show()
    sys.exit(app.exec_())