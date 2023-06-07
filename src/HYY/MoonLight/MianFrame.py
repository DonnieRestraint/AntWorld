import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QSize, Qt, QRectF, QRect, QEvent, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

from AppAlg.Move import DragAlg
from AppStyle.StyleLoader import Loader
from AppStyle.StyleQss import StyleQss
from Dandelion import Icon, Pixmap
from MoonLight.DisplayBox import BrowserWidget
from MoonLight.Logo import LogoWidgetUp, LogoWidgetDown
from MoonLight.NavBar import NavWidget
from MoonLight.MenuBar import TitleWidget
from PyQt5.QtGui import QMouseEvent
import Resource.resource_qrc
from AppStyle.StyleQss import StyleQss
import cgitb

DEBUG = True

cgitb.enable(format='text') if DEBUG else ...


class MainFrame(QMainWindow, DragAlg):

    def __init__(self):
        super(MainFrame, self).__init__()
        self.setObjectName("MainFrame")
        # 设置标题栏的icon
        self.setWindowIcon(Icon(Pixmap(":/images/moon.png")))
        self.setWindowTitle("一月寒")
        self.setStyleSheet(StyleQss.get_qss())
        self.setSize()
        # Loader.attrAttach(self)
        # Loader.boundAttach(self)
        Loader.flagDetach(self)
        self.addWidget()
        self.setMouseTracking(True)

    def setSize(self, size=None):
        if not size:
            desktop = QApplication.desktop()
            # PyQt5.QtCore.QSize(1920, 1080)
            width, height = int(desktop.width() * 0.6), int(desktop.height() * 0.6)
            print(width, height)
            self.setFixedSize(QSize(width, height))
        else:
            self.setSize(*size)

    def addWidget(self):
        self.logo = LogoWidgetUp(self)
        self.navBar = NavWidget(self)
        self.logo_bottom = LogoWidgetDown(self)
        self.MenuBar = TitleWidget(self)
        self.browserFrame = BrowserWidget(self)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        width = self.width()
        height = self.height()

        self.logo.setGeometry(QRect(0, 0, self.setInt(width, 0.15), self.setInt(width, 0.15) - 1))
        self.navBar.setGeometry(QRect(0, self.setInt(width, 0.15), self.setInt(width, 0.15), height - self.setInt(width, 0.3)))
        self.logo_bottom.setGeometry(QRect(0, height - self.setInt(width, 0.15), self.setInt(width, 0.15), self.setInt(width, 0.15)))
        self.MenuBar.setGeometry(QRect(self.setInt(width, 0.15), 0, self.setInt(width, 0.85) + 1, self.setInt(height, 0.05)))
        self.browserFrame.setGeometry(QRect(self.setInt(width, 0.15), self.setInt(height, 0.06), self.setInt(width, 0.85) + 1, self.setInt(height, 0.94)+1))

    def setInt(self, length, ratio):
        return int(length * ratio)

    def eventFilter(self, obj: 'QObject', event: 'QEvent') -> bool:
        """使用事件过滤器需要继承自QObject"""
        if event.type() in [QEvent.Type.MouseButtonPress, QEvent.Type.MouseMove, QEvent.Type.MouseButtonRelease]:
            # event.accept()
            if event.type() == QEvent.Type.MouseButtonPress:
                # event = QMouseEvent(
                #     QEvent.MouseButtonPress,
                #     event.pos(),
                #     Qt.LeftButton, Qt.LeftButton,
                #     Qt.NoModifier
                # )
                DragAlg.mousePressEvent(self, event)
            if event.type() == QEvent.Type.MouseMove:
                # event = QMouseEvent(
                #     QEvent.MouseMove,
                #     event.pos(),
                #     Qt.NoButton,
                #     Qt.NoButton,
                #     Qt.NoModifier
                # )
                # 返回true表示该事件不再进一步处理
                DragAlg.mouseMoveEvent(self, event)
                return True
            if event.type() == QEvent.Type.MouseButtonRelease:
                # event = QMouseEvent(
                #     QEvent.MouseButtonRelease,
                #     event.pos(),
                #     Qt.LeftButton,
                #     Qt.NoButton,
                #     Qt.NoModifier
                # )
                DragAlg.mouseReleaseEvent(self, event)
        # 返回false，表示其余事件交还给目标对象处理，本例应返回false, True表示不再进一步处理
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainFrame()
    frame.show()
    sys.exit(app.exec())
