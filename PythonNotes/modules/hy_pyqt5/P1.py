from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent


class DragWindow(object):
    """drag and drop the window mode"""
    def __init__(self):
        self.init_param()

    def init_param(self):
        self._isTracking = False
        self._startPos = None
        self._endPos = None

    def mousePressEvent(self, e: QMouseEvent):
        """mouse press"""
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())
        else:
            self._isTracking = False

        if self.isMaximized():
            self.init_param()

    def mouseMoveEvent(self, e: QMouseEvent):
        if self._isTracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self.init_param()