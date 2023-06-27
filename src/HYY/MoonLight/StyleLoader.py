from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
import re

DEBUG = True
DevStyle = True


class Loader(object):
    @staticmethod
    def flagDetach(widget: QtWidgets.QWidget):
        # 隐藏窗口标志, 隐藏任务栏
        widget.setWindowFlags(Qt.FramelessWindowHint | Qt.SplashScreen)

    @staticmethod
    def attrAttach(widget: QtWidgets.QWidget):
        # 窗口属性透明
        widget.setAttribute(Qt.WA_TranslucentBackground)

    @staticmethod
    def boundAttach(widget: (QtWidgets.QWidget, QtWidgets.QBoxLayout), interval=(0, 0, 0, 0)):
        widget.setContentsMargins(*interval)

    @staticmethod
    def spaceAttach(layout: QtWidgets.QBoxLayout, interval=0):
        layout.setSpacing(interval)

    @staticmethod
    def passQss(cls):
        if not hasattr(cls, "objectStyle"):
            return
        else:
            cls.setStyleSheet(cls.objectStyle % Loader.getQssAttr())
        if DevStyle and DEBUG:
            print(cls.objectStyle)
        else:
            objectNameRegex = r"#(?P<objectName>[a-zA-z0-9\s]*){"
            rl_list = re.findall(objectNameRegex, cls.objectStyle)
            if rl_list:
                print(cls.__class__, "\r\n    ", rl_list)

    @staticmethod
    def getQssAttr():
        font_normal = 400  # 正常字体
        font_bold = 700  # 加粗字体
        white = (255, 255, 255, 255)
        font_family = "monospace"
        opacity = 255
        return {
            "opacity": opacity,
            "font_normal": font_normal,
            "font_bold": font_bold,
            "font_family": font_family,
            "white": white,
        }
