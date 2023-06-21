from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QLabel, QHBoxLayout, QWidget, QFrame, QVBoxLayout, QScrollArea

from MoonLight import Loader
from MoonLight.BaseWidgets.TimeCycle import DateTimeEdit


class SettingWidget(QWidget):
    listWidget = None
    objectStyle = """
        QPushButton#settingButton{
            padding:0px;
            margin:0px;
            background-color: rgba(60, 56, 57, 255);
            color:rgba(118, 101, 85, 255);

            border: 0px solid rgba(83, 69, 69, 255);
            border-radius:0px;

            font-size: 18px;
            font-weight: 400;
            font-family:monospace;
        }
        QPushButton#settingButton:focus {
            background: rgba(67, 60, 58, 200);
            color:rgba(118, 101, 85,255);
        }
        QScrollArea#settingScroll{
            padding:0px;
            margin:0px;
            border-radius: 0px;
            border: 0px solid rgba(255,255,255,0);
            background-color:rgba(53, 47, 45, 255);
        }
        QWidget#rightWidget{
            background-color:rgba(53, 47, 45, 0);
        }
        QWidget#leftWidget{
            background-color:rgba(60, 56, 57, 255);
        }
        QWidget#settingWidget{
            background-color:rgba(67, 60, 58, 200);
        }
        QFrame#splitLine{
            background-color:rgba(118, 101, 85, 255);
        }
        QLabel#labelText{
            color: rgba(118, 101, 85, 255);
            font-size: 18px;
            font-weight: 400;
            font-family:monospace;
        }
        QPushButton#onBeSure{
            background-color:rgba(67, 60, 58, 255);
            color:rgba(118, 101, 85, 255);
        }
        QPushButton#close_btn {
            border-image: url(:/images/set_close.png) no-repeat 0px 0px;
        }
        """
    name_dict = {
        "YYH1": [
            {"name": "Daily Cycle1", "type_edit": DateTimeEdit},
            {"name": "Daily Cycle", "type_edit": DateTimeEdit},
         ],
        "YYH2": [{"name": "Daily Cycle2", "type_edit": DateTimeEdit}],
    }

    def layoutFrame(self):
        self.leftWidget = QWidget(self)
        self.leftWidget.setObjectName("leftWidget")
        self.left_layout = QVBoxLayout(self)
        Loader.spaceAttach(self.left_layout)
        Loader.boundAttach(self.left_layout)
        self.fill_left_layout()
        self.leftWidget.setLayout(self.left_layout)

        self.rightScroll = QScrollArea(self)
        self.rightScroll.setObjectName("settingScroll")
        self.rightScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rightScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rightScroll.verticalScrollBar().valueChanged.connect(self.on_settingScroll_valueChanged)
        self.rightWidget = QWidget()
        self.rightWidget.setObjectName("rightWidget")
        self.rightLayout = QVBoxLayout()
        self.rightWidget.setLayout(self.rightLayout)
        self.fill_right_layout()
        self.rightScroll.setWidget(self.rightWidget)
        Loader.boundAttach(self.rightLayout)
        Loader.spaceAttach(self.rightLayout)
        Loader.boundAttach(self.rightWidget)
        self.close_button = QPushButton(self.rightScroll)
        self.close_button.setObjectName("close_btn")
        self.close_button.clicked.connect(self.close)

    def fill_left_layout(self):
        for name in self.name_dict:
            button = QPushButton(name, self.leftWidget)
            button.setObjectName("settingButton")
            button.setCheckable(True)
            button.clicked.connect(self.on_settingButton_clicked)
            self.left_layout.addWidget(button)
            line = QFrame()
            line.setObjectName("splitLine")
            line.setFixedHeight(1)
            # line.setFrameShape(QFrame.HLine)
            self.left_layout.addWidget(line)

        self.left_layout.addStretch(1)

        # line = QFrame()
        # line.setObjectName("splitLine")
        # line.setFixedHeight(1)
        # # line.setFrameShape(QFrame.HLine)
        # self.left_layout.addWidget(line)
        Loader.spaceAttach(self.left_layout)

    def fill_right_layout(self):
        for name, widget_list in self.name_dict.items():
            for info_dict in widget_list:
                self.set_right_layout(info_dict)

    def set_right_layout(self, info_dict):
        widget = QWidget(self.rightScroll)
        h_layout = QHBoxLayout()
        h_layout.setContentsMargins(40, 20, 0, 0)  # left, up, right, low
        Loader.spaceAttach(h_layout, interval=30)
        widget.setLayout(h_layout)

        text = info_dict.get("name", "")
        type_edit = info_dict.get("type_edit", "")
        if text:
            label = QLabel(text, widget)
            label.setObjectName("labelText")
            if not type_edit:
                h_layout.addWidget(label, 0, Qt.AlignHCenter)
            else:
                h_layout.addWidget(label, 0, Qt.AlignHCenter)
        if type_edit:
            edit = type_edit(widget)
            h_layout.addWidget(edit, 0, Qt.AlignHCenter)
            btn = QPushButton("BeSure", widget)
            btn.clicked.connect(edit.on_BeSure_clicked)
            btn.setObjectName("onBeSure")
            h_layout.addWidget(btn, 0, Qt.AlignHCenter)

        self.rightLayout.addWidget(widget)

    def on_settingButton_clicked(self):
        """点击按钮移动右边滑块的值，未实现到理想效果"""
        text = self.sender().text()
        index = list(self.name_dict).index(text)
        button = self.left_layout.itemAt(index).widget()
        # print(index, text, button)
        button_count = len(self.name_dict.keys())
        self.rightScroll.verticalScrollBar().setValue(int(index/button_count*self.h))

    def on_settingScroll_valueChanged(self, h_val):
        """移动右边滑块改变被聚焦的按钮，未实现到理想效果"""
        # print(self.left_layout.count(), h_val, self.h)
        button_count = len(self.name_dict.keys())
        for i in range(button_count):
            if h_val / self.h > (i+1)/button_count:
                print(h_val, (i+1)/button_count)
                self.left_layout.itemAt(i*2).widget().setFocus()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        width, height = self.width(), self.height()
        self.w, self.h = width, height
        # print(width, width*0.25, width*0.75)
        self.leftWidget.setGeometry(0, 0, int(width * 0.25), height)
        for i in range(self.left_layout.count()):
            widget = self.left_layout.itemAt(i).widget()
            if isinstance(widget, QPushButton):
                widget.setFixedHeight(self.l_button_h)
        self.rightScroll.setGeometry(int(width * 0.25), 0, width - int(width * 0.25), height)
        self.close_button.setGeometry(self.rightScroll.width() - 30, 0, 30, 30)

    def __init__(self, parent=None):
        super(SettingWidget, self).__init__(parent)
        self.setObjectName("settingWidget")
        Loader.passQss(self)
        Loader.flagDetach(self)
        Loader.boundAttach(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.layoutFrame()
        self.w = 0
        self.h = 0
        self.l_button_h = 40
        self.show()
        # self.rightLayout.itemAt(2).widget().click()
        # self.left_layout.itemAt(2).widget().click()
        self.left_layout.itemAt(0).widget().setFocus()
