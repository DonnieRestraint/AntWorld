from PyQt5 import QtGui
from PyQt5.QtCore import QSize, QRect, QEvent
from PyQt5.QtWidgets import QApplication, QMainWindow

from AppAlgorithm.Move import DragAlg
from MoonLight.StyleLoader import Loader
from MoonLight.DynamicWidget.expandWidget import BrowserWidget
from MoonLight.LogoWidget.logo import LogoWidgetUp, LogoWidgetDown
from MoonLight.NavWidget.navBar import NavWidget
from MoonLight.SettingWidget.menuWidget import TitleWidget
from PyQt5.QtGui import QPixmap, QIcon
from Resource import resource_qrc


class MainFrame(QMainWindow, DragAlg):
    objectStyle = """
        QMainWindow#MainFrame{
            border-image: url(:/images/bg001.png) no-repeat 0px 0px;
        }"""

    def __init__(self):
        super(MainFrame, self).__init__()
        self.setObjectName("MainFrame")
        self.defaultWindowFlags = self.windowFlags()
        Loader.passQss(self)
        # 设置标题栏的icon
        self.setWindowIcon(QIcon(QPixmap(":/images/moon.png")))
        self.setWindowTitle("一月寒")
        self.setSize()
        # Loader.attrAttach(self)
        # Loader.boundAttach(self)
        Loader.flagDetach(self)
        self.addWidget()
        self.setMouseTracking(True)

    def setSize(self, size=None):
        if not size:
            desktop = QApplication.desktop()
            # PyQt5.QtCore.QSize(1920, 1080) - > 1152 648
            width, height = int(desktop.width() * 0.6), int(desktop.height() * 0.6)
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

    def eventFilter(self, source, event) -> bool:
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

    def restoreFlags(self):
        """默认窗口状态的恢复，需要先保存默认窗口状态"""
        isVisible = self.isVisible()
        self.setWindowFlags(self.defaultWindowFlags)    # 状态变化会隐藏窗口
        self.MenuBar.hide()
        if isVisible:
            self.setVisible(True)


