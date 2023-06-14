from PyQt5 import QtGui
from PyQt5.QtCore import QRect, QRectF
from PyQt5.QtGui import QPainter, QBrush, QColor, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel
from MoonLight.StyleLoader import Loader
from Resource import resource_qrc


class LogoWidgetDown(QWidget):

    def __init__(self, parent=None):
        super(LogoWidgetDown, self).__init__(parent)
        self.label = QLabel(self)
        self.setObjectName("LogoBWidget")
        self.bg_color = (57, 55, 57, 255)
        self.one_degree = 16
        Loader.passQss(self)
        Loader.attrAttach(self)
        Loader.boundAttach(self)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        super(LogoWidgetDown, self).paintEvent(a0)
        painter = QPainter()
        painter.begin(self)
        pixmap = QPixmap(":/images/moon.png")
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        scale = 0.5
        self.label.setGeometry(self.width() / 2 * (1 - scale)-1,
                               self.height() / 2 * (1 - scale)-1,
                               self.width() * scale+1,
                               self.height() * scale+1
                               )
        # 整体填充背景色
        bg_circle = LogoWidgetUp.get_scale(self.rect(), 1.5)
        painter.setBrush(QBrush(QColor(*self.bg_color)))
        painter.setPen(QColor(*self.bg_color))
        for b in range(16 * 4):
            painter.drawChord(bg_circle, b * 360 / 4, 16 * 141)  # area*1.5画圆弧
        painter.end()


class LogoWidgetUp(QWidget):
    def __init__(self, parent=None):
        super(LogoWidgetUp, self).__init__(parent)
        self.setObjectName("LogoWidget")
        self.moon_light_color = (255, 255, 204, 200)
        self.bg_color = (57, 55, 57, 255)
        self.sun_light_color = self.bg_color
        self.one_degree = 16
        Loader.passQss(self)
        Loader.attrAttach(self)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        super(LogoWidgetUp, self).paintEvent(a0)

        painter = QPainter()
        # 设置反锯齿
        painter.setRenderHint(QPainter.Antialiasing, True)
        brush = QBrush()
        painter.begin(self)
        self.DrawMoon(painter, brush, self.rect())
        painter.end()

    def DrawMoon(self, painter: QPainter, brush: QBrush, area: (QRect, QRectF)):
        # 绘制区域, 起始的角度, 结束的角度
        # print(area.width())
        # print(area.height())
        bg_circle = self.get_scale(area, 1.5)
        # print(bg_circle)
        great_circle = self.get_scale(area, 0.5)
        small_circle = self.get_scale(area, 0.3)

        # 整体填充背景色
        painter.setBrush(QBrush(QColor(*self.bg_color)))
        painter.setPen(QColor(*self.bg_color))
        for b in range(16 * 4):
            # painter.drawChord(bg_circle, b * 360 / 4, 16 * 120)  # area*1画圆弧
            painter.drawChord(bg_circle, b * 360 / 4, 16 * 142)  # area*1.5画圆弧

        # 外圆填充背景色
        painter.setBrush(QBrush(QColor(*self.moon_light_color)))
        painter.setPen(QColor(*self.moon_light_color))
        painter.drawPie(great_circle, self.one_degree * 15, self.one_degree * 360)  # 扇形面积填充
        # painter.drawArc(new_area, 16 * 15, 16 * 330)  # 画圆弧
        # painter.drawChord(new_area, 16 * 15, 16 * 50) #  圆弧的拱形面积填充

        # 内圆填充背景色
        painter.setBrush(QBrush(QColor(*self.sun_light_color)))
        painter.setPen(QColor(*self.sun_light_color))
        small_circle = QRectF(small_circle.left() + small_circle.width() / 3, small_circle.top(),
                              small_circle.width(), small_circle.height())
        painter.drawPie(small_circle, self.one_degree * 15, self.one_degree * 360)  # 扇形面积填充
        # painter.eraseRect(QRectF(50, 0, 50, 120))

    @staticmethod
    def get_scale(area: (QRectF, QRect), scale: float):
        point_l, point_t = area.left(), area.top()
        point_r, point_b = area.right(), area.bottom()
        width = area.width()
        height = area.height()
        center_x, center_y = int(point_l / 2 + point_r / 2), int(point_t / 2 + point_b / 2)
        # print(point_l, center_x, point_r, point_t, center_y, point_b)
        new_l = center_x - width / 2 * scale
        new_r = center_x + width / 2 * scale
        new_t = center_y - height / 2 * scale
        new_b = center_y + height / 2 * scale
        return QRectF(new_l, new_t, new_r - new_l, new_b - new_t)


if __name__ == '__main__':
    import sys
    from PyQt5 import QtGui
    from PyQt5.QtWidgets import QWidget, QApplication

    app = QApplication(sys.argv)
    frame = LogoWidgetUp(None)
    frame.show()
    sys.exit(app.exec())
