import math
from datetime import datetime

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QLineF, QRect, QPointF, QSize, QMetaObject, pyqtSlot
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtWidgets import QApplication
from AppAlgorithm.WindowOperate import HYOperate
from MoonLight.BaseWidgets.TimeCycle import DateTimeEdit
from MoonLight.SettingWidget.settingFrame import SettingWidget
from MoonLight.StyleLoader import Loader
from MoonLight.LogoWidget.logo import LogoWidgetUp
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QFrame, QHBoxLayout, QVBoxLayout, QScrollArea


class IcoButton(QWidget):
    objectStyle = """
        QWidget#title_widget {
            background: rgba(255,255,255,0);
        }
        """

    def __init__(self, parent=None, draw=None):
        super(IcoButton, self).__init__(parent)
        Loader.passQss(self)
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
    objectStyle = """
        QPushButton#minimize_btn {
            border-image: url(:/images/minimize.png) no-repeat 0px 0px;
        }
        QPushButton#settingWidget {
            border-image: url(:/images/setting.png) no-repeat 0px 0px;
        }
        QPushButton#close_btn {
            border-image: url(:/images/close.png) no-repeat 0px 0px;
        }
        QLabel#title_text {
            padding:0px;
            margin:0px;
            color:rgba(63,63,63,255);
            font-size:18px;
            font-weight: %(font_bold)s;
            font-family:%(font_family)s;
        }
        """

    def __init__(self, parent=None):
        super(TitleWidget, self).__init__(parent)
        self.offset_d = 10
        self.frame = parent
        self.setMinimumSize(QSize(200, 35))
        self.layout_widget()
        Loader.passQss(self)
        Loader.attrAttach(self)
        # 使用信号装饰器
        QMetaObject.connectSlotsByName(self)

    def layout_widget(self):
        self.title_widget = QWidget(self)
        self.title_widget.setObjectName("title_widget")

        self.title_label = QLabel(self.title_widget)
        self.title_label.setObjectName("title_text")
        self.title_label.setText("One Month Seven")

        self.mini_button = QPushButton(self.title_widget)
        self.mini_button.setObjectName("minimize_btn")
        self.mini_button.clicked.connect(lambda x: self.parent().showMinimized())

        self.setting_button = QPushButton(self.title_widget)
        self.setting_button.setObjectName("settingWidget")

        self.close_button = QPushButton(self.title_widget)
        self.close_button.setObjectName("close_btn")
        self.close_button.clicked.connect(self.close_all)

    def close_all(self):
        if self.parent():
            self.parent().trayIcon.setVisible(False)
        QApplication.instance().quit()

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
        p = self.parent()
        width_start = p.pos().x() + int(p.width()/2)
        height_start = p.pos().y() + int(p.height()/2)

        self.sw = SettingWidget(self.parent())
        self.sw.setGeometry(width_start - 300, height_start - 200, 650, 400)

    def exe_win_cmd(self):
        str_datetime = DateTimeEdit.get_anchorTime(DateTimeEdit)
        if not str_datetime:
            return
        record_datetime = datetime.strptime(str_datetime, DateTimeEdit.dt_strftime)
        record_time = record_datetime - datetime(year=record_datetime.year, month=record_datetime.month, day=record_datetime.day)
        cur_datetime = datetime.now()
        cur_time = cur_datetime - datetime(year=cur_datetime.year, month=cur_datetime.month, day=cur_datetime.day)
        cr_timeout = (cur_time - record_time).seconds
        rc_timeout = (record_time - cur_time).seconds
        one_minute = 60
        if rc_timeout < one_minute:
            self.title_label.setText(str(rc_timeout))
        if cr_timeout > 60:
            return
        else:
            hy = HYOperate()
            hy.close_windows()
