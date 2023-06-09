import math
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QLineF, QRect, QPointF, QSize, QMetaObject, pyqtSlot
from PyQt5.QtGui import QPainter, QBrush, QColor, QPen, QPolygon, QMouseEvent

from AppStyle.StyleLoader import Loader
from Dandelion.time_cycle import DateTimeEdit
from MoonLight.Logo import LogoWidgetUp
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QFrame, QListWidget, QListWidgetItem, QHBoxLayout, \
    QVBoxLayout, QScrollArea, QGridLayout
from Resource import resource_qrc


class IcoButton(QWidget):
    def __init__(self, parent=None, draw=None):
        super(IcoButton, self).__init__(parent)
        self.type = {"mini": self.mini_ico, "close": self.close_ico, "setting": self.setting_ico}
        self.draw = self.type.get(draw, None) if draw else None
        width, height = self.width(), self.height()
        self.setFixedSize(50, 50)

    def mini_ico(self, painter: QPainter):
        #  颜色， 笔宽， 实线， 平顶， 平滑连接
        pen = QPen(Qt.gray, 3, Qt.SolidLine, Qt.FlatCap, Qt.RoundJoin)
        painter.setPen(pen)
        line = QLineF(self.width() * 0.1, self.height() / 2, self.width() * 0.8, self.height() / 2)
        painter.drawLine(line)

    def close_ico(self, painter: QPainter):
        pass

    def setting_ico(self, painter: QPainter):
        points = []
        rx, ry = self.width() / 2, self.height() / 2
        for i, d in enumerate(range(0, 360, 30)):
            if i % 2 == 1:
                r = self.height() / 2
            else:
                r = self.height() / 2.5

            point = QPointF(rx + r * math.cos(2 * math.pi / 360 * d), ry + r * math.sin(2 * math.pi / 360 * d))
            points.append(point)
        #  颜色， 笔宽， 实线， 圆顶， 平滑连接
        pen = QPen(Qt.gray, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        painter.setPen(pen)
        painter.drawPolygon(*points)
        # polygon = QPolygon()
        # polygon.setPoints(1,1,2,2,3,3)
        # painter.drawPolygon(polygon)

        pen = QPen(Qt.gray, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        painter.setPen(pen)
        area_m = LogoWidgetUp.get_scale(QRect(0, 0, self.width(), self.height()), 0.1)
        print(area_m, rx, ry)
        painter.drawArc(area_m, 360 * 16, 360 * 16)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        super(IcoButton, self).paintEvent(a0)
        painter = QPainter()
        # 设置反锯齿
        painter.setRenderHint(painter.Antialiasing)
        brush = QBrush()
        painter.begin(self)
        self.draw(painter)
        painter.end()


class TitleWidget(QWidget):
    def __init__(self, parent=None):
        super(TitleWidget, self).__init__(parent)
        self.offset_d = 10
        self.frame = parent
        self.setMinimumSize(QSize(200, 35))
        self.layout_widget()
        Loader.attrAttach(self)
        # 使用信号装饰器
        QMetaObject.connectSlotsByName(self)

    def layout_widget(self):
        self.title_widget = QWidget(self)
        self.title_widget.setObjectName("title_widget")

        self.title_label = QLabel(self.title_widget)
        self.title_label.setObjectName("title_text")
        self.title_label.setText("这是一个title!")

        self.mini_button = QPushButton(self.title_widget)
        self.mini_button.setObjectName("minimize_btn")
        self.mini_button.clicked.connect(lambda x: self.parent().showMinimized())

        self.setting_button = QPushButton(self.title_widget)
        self.setting_button.setObjectName("settingWidget")

        self.close_button = QPushButton(self.title_widget)
        self.close_button.setObjectName("close_btn")
        self.close_button.clicked.connect(self.parent().close)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        width, height = self.width(), self.height()

        self.title_widget.setGeometry(0, 0, width, height)
        self.title_label.setGeometry(height, 0, width * 0.2, height)
        self.mini_button.setGeometry(width - height * 3 - self.offset_d, 0, height, height)
        self.setting_button.setGeometry(width - height * 2 - self.offset_d, 0, height, height)
        self.close_button.setGeometry(width - height - self.offset_d, 0, height, height)

    @pyqtSlot()
    def on_settingWidget_clicked(self):
        """on_settingWidget_clicked
        开放信号装饰器：QMetaObject.connectSlotsByName(self)
        on：固定的函数开头
        setObjectName：设置的对象名settingWidget
        内置信号：clicked
        """
        self.sw = SettingWidget()


class SettingWidget(QWidget):
    listWidget = None
    settingStyle = """
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
                background-color:rgba(255,255,255,0);
            }
            QWidget#rightWidget{
                background-color:rgba(255, 255, 255, 0);
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
                background-color:rgba(67, 60, 58);
                color:rgba(118, 101, 85, 255);
            }
            """
    name_dict = {
        "YYH": [{"name": "Daily Cycle", "type_edit": DateTimeEdit}, {"name": "AA", "type_edit": ""}],
        "视频": [{"name": "一天天", "type_edit": ""}, {"name": "BB", "type_edit": ""}],
        "音频": [{"name": "一月月", "type_edit": ""}, {"name": "CC", "type_edit": ""}],
        "音频1": [{"name": "一月月", "type_edit": ""}, {"name": "CC", "type_edit": ""}],
        "音频2": [{"name": "一月月", "type_edit": ""}, {"name": "CC", "type_edit": ""}],
        "音频3": [{"name": "一月月", "type_edit": ""}, {"name": "CC", "type_edit": ""}],
        "音频4": [{"name": "一月月", "type_edit": ""}, {"name": "CC", "type_edit": ""}],
        "音频5": [{"name": "一月月", "type_edit": ""}, {"name": "CC", "type_edit": ""}],
        "音频6": [{"name": "一月月", "type_edit": ""}, {"name": "CC", "type_edit": ""}],
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

        self.rightWidget = QWidget()
        self.rightWidget.setObjectName("rightWidget")
        self.rightLayout = QVBoxLayout()
        self.rightWidget.setLayout(self.rightLayout)
        self.fill_right_layout()
        self.rightScroll.setWidget(self.rightWidget)
        Loader.boundAttach(self.rightLayout)
        Loader.spaceAttach(self.rightLayout)

        Loader.boundAttach(self.rightWidget)

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

        line = QFrame()
        line.setObjectName("splitLine")
        line.setFixedHeight(1)
        # line.setFrameShape(QFrame.HLine)
        self.left_layout.addWidget(line)

        button = QPushButton("取消", self.leftWidget)
        button.setObjectName("settingButton")
        button.clicked.connect(self.close)
        self.left_layout.addWidget(button)
        Loader.spaceAttach(self.left_layout)

    def fill_right_layout(self):
        for name, widget_list in self.name_dict.items():
            for info_dict in widget_list:
                self.set_right_layout(info_dict)

    def set_right_layout(self, info_dict):
        widget = QWidget(self.rightWidget)
        Loader.attrAttach(widget)
        h_layout = QHBoxLayout()
        h_layout.setContentsMargins(20, 20, 20, 0)
        Loader.spaceAttach(h_layout, interval=20)
        widget.setLayout(h_layout)

        text = info_dict.get("name", "")
        type_edit = info_dict.get("type_edit", "")
        if text:
            label = QLabel(text, widget)
            label.setObjectName("labelText")
            if not type_edit:
                h_layout.addWidget(label, 1, Qt.AlignHCenter)
            else:
                h_layout.addWidget(label, 1, Qt.AlignRight)
        if type_edit:
            edit = type_edit(widget)
            h_layout.addWidget(edit, 1, Qt.AlignLeft)
            btn = QPushButton("BeSure", widget)
            btn.clicked.connect(edit.onBeSure)
            btn.setObjectName("onBeSure")
            h_layout.addWidget(btn, 1, Qt.AlignHCenter)

        self.rightLayout.addWidget(widget)

    def on_settingButton_clicked(self):
        text = self.sender().text()
        index = list(self.name_dict).index(text)
        button = self.left_layout.itemAt(index).widget()
        print(index, text, button)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        width, height = self.width(), self.height()
        self.leftWidget.setGeometry(0, 0, int(width * 0.25), height)
        for i in range(self.left_layout.count()):
            widget = self.left_layout.itemAt(i).widget()
            if isinstance(widget, QPushButton):
                widget.setFixedHeight(40)
        self.rightScroll.setGeometry(int(width * 0.25), 0, width - int(width * 0.25), height)

    def __init__(self):
        super(SettingWidget, self).__init__()
        self.setFixedSize(600, 400)
        self.setObjectName("settingWidget")
        Loader.flagDetach(self)
        Loader.boundAttach(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.setStyleSheet(self.settingStyle)
        self.layoutFrame()
        self.show()
        print(self.left_layout.itemAt(2).widget().click())
        print(self.left_layout.itemAt(2).widget().setFocus())


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QWidget, QApplication

    app = QApplication(sys.argv)
    frame = TitleWidget(None)
    frame.show()
    sys.exit(app.exec())
