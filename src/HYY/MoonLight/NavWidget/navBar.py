from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QPushButton
from MoonLight.StyleLoader import Loader


class NavWidget(QWidget):
    objectStyle = """
        QScrollArea#nav_bar{
            border-radius: 0px;
            border: 0px solid ;
            border-color: rgba(255,255,255,255);
            background-color:rgba(57, 55, 57, 255);
        }
        QPushButton#NavPushButton{
            background-color: rgba(57, 55, 57, 255);
            border-radius:0px;
            padding:0px;
            margin:0px;
            border:0px solid rgba(150,120,100, 255);
            color:rgba(118, 101, 91, 255);
            font-size:18px;
            font-weight: %(font_bold)s;
            font-family:%(font_family)s;
        }
        QPushButton#NavPushButton:hover {
            background: rgba(240, 255, 250, 255);
            color:rgba(118, 101, 91, 255);
            font-size:18px;
            font-weight: %(font_bold)s;
            font-family:%(font_family)s;
        }
        QPushButton#NavPushButton:pressed {
            background: rgba(255, 255, 255, 255);
            color:rgba(118, 101, 91, 255);
            font-size:18px;
            font-weight: %(font_bold)s;
        }
        QPushButton#NavPushButton:focus {
            background: rgba(255, 255, 255, 255);
            color:rgba(118, 101, 91, 255);
        }
        """

    def __init__(self, parent=None):
        super(NavWidget, self).__init__(parent)
        self.topfiller = QWidget()
        self.scroll = QScrollArea()
        self.scroll.setObjectName("nav_bar")
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidget(self.topfiller)
        self.items_layout = QVBoxLayout()
        self.topfiller.setLayout(self.items_layout)
        self.normal_layout = QVBoxLayout()
        self.normal_layout.addWidget(self.scroll)
        self.setLayout(self.normal_layout)
        self.init_bound()
        self.layout_scroll()
        Loader.passQss(self)

    def init_bound(self):
        # Nav背景窗口
        # Loader.attrAttach(self.scroll)
        Loader.attrAttach(self.topfiller)
        Loader.boundAttach(self.topfiller)
        Loader.boundAttach(self.scroll)
        Loader.boundAttach(self.normal_layout)
        Loader.boundAttach(self.items_layout)
        Loader.spaceAttach(self.items_layout)

    def layout_scroll(self):

        item_list = ["YYH", "视频", "音频"] * 1
        self.item_height = 42
        self.item_border = 0
        self.color = QColor(121, 44, 121, 255)

        for filename in item_list:
            button = QPushButton(self.topfiller)
            button.setObjectName("NavPushButton")
            # 使用父窗口的eventFilter函数进行处理
            button.installEventFilter(self.parent())
            button.setText(str(filename))
            button.setCheckable(True)
            button.clicked.connect(self.button_click)
            self.items_layout.addWidget(button)

    def button_click(self, e: QtCore.QEvent):
        source = self.sender()
        print(source.text())

    def resizeEvent(self, a0) -> None:
        super(NavWidget, self).resizeEvent(a0)

        # 对滚动条区域进行尺寸修正
        self.topfiller.setFixedWidth(self.width())
        self.topfiller.setFixedHeight(self.items_layout.count() * self.item_height)
        # 对按钮进行尺寸修正
        for item_index in range(self.items_layout.count()):
            self.items_layout.itemAt(item_index).widget().setFixedSize(self.topfiller.width(), self.item_height)

