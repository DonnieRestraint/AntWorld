# 好处在于可以把子控件放在一起，且重复使用，只需调用这个包就好了
from PyQt5.Qt import *
import math
import random


class PaintArea(QWidget):  # 画图类
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setPalette(QPalette(QColor(240, 240, 240)))  # 设置背景颜色
        self.setAutoFillBackground(True)  # 设置窗口自动填充背景
        self.runway_direction = 45  # 跑道角度
        self.wind_direction = 90  # 初始风向
        self.wind_speed = 0  # 初始风速

    def paintEvent(self, event):  # 重写绘图事件
        self.rect_base = QRect(20, 20, self.width() - 40, self.width() - 40)  # 设置了画图的区域
        self.painter_base = QPainter()  # 底图绘图类
        self.painter_base.begin(self)
        # 底图
        self.painter_base.setBrush(QColor(100, 100, 255))
        self.painter_base.setPen(QPen(QColor(255, 255, 255), 10, Qt.SolidLine))
        self.painter_base.drawEllipse(self.rect_base)
        self.painter_base.end()

        # 计算跑道起始结束坐标
        self.fromX_runway_direction, self.fromY_runway_direction, self.toX_runway_direction, self.toY_runway_direction = self.calculatePoint(
            self.runway_direction)

        self.painter = QPainter()  # 画图类
        self.painter.begin(self)
        # 画刻度盘
        self.drowLines(self.fromX_runway_direction, self.fromY_runway_direction, self.toX_runway_direction,
                       self.toY_runway_direction, width=self.width() / 5)  # 画跑道
        self.drowLines(20, int(self.height() / 2), self.width() - 20, int(self.height() / 2), width=2,
                       color=QColor(145, 146, 171))  # 画水平线
        self.drowLines(int(self.width() / 2), 20, int(self.width() / 2), self.height() - 20, width=2,
                       color=QColor(145, 146, 171))  # 画垂直线
        self.drawEllipses(self.rect_base)  # 画边界园
        self.drawTexts(QRect(5, 0, self.width(), 30), "0°", fontsize=int(self.width() / 15))  # 画0°
        self.drawTexts(QRect(5, self.height() - 30, self.width(), 30), "180°", fontsize=int(self.width() / 15))  # 画180°
        self.drawTexts(QRect(0, 0, 70, self.height()), "270°", fontsize=int(self.width() / 15))  # 画270°
        self.drawTexts(QRect(self.width() - 40, 0, 40, self.height()), "90°", fontsize=int(self.width() / 15))  # 画90°

        self.drawTexts(self.rect_base, self.wind_speed, fontsize=int(self.width() / 3))  # 画风速
        # 计算风向箭头四个点坐标
        po1_x, po1_y, a, b = self.calculatePoint1(self.wind_direction - 7)
        po3_x, po3_y, a, b = self.calculatePoint1(self.wind_direction + 7)
        a, b, po4_x, po4_y = self.calculatePoint(self.wind_direction)
        po1 = QPoint(po1_x, po1_y)
        po2 = QPoint(int(self.width() / 2), int(self.height() / 2))
        po3 = QPoint(po3_x, po3_y)
        po4 = QPoint(po4_x, po4_y)
        points = [po1, po2, po3, po4]
        # 画风向箭头
        self.drawPolygons(points)

        self.painter.end()  # 结束

    # 从外部获取风向
    def setWindDirection(self, wind_direction):
        self.wind_direction = wind_direction

    # 从外部获取风速
    def setWindSpeed(self, wind_speed):
        self.wind_speed = wind_speed

    # 画线
    def drowLines(self, fromX, fromY, toX, toY, width=10, color=QColor(91, 91, 170)):
        pen = QPen(color, width, Qt.SolidLine)
        self.painter.setPen(pen)
        self.painter.drawLine(fromX, fromY, toX, toY)

    # 画圆
    def drawEllipses(self, rect, width=10, color=QColor(180, 180, 220)):
        pen = QPen(color, width, Qt.DashLine)
        self.painter.setPen(pen)
        self.painter.drawEllipse(rect)

    # 画字
    def drawTexts(self, rect, ws, fontsize=100):
        self.painter.setPen(QColor(0, 255, 0))
        self.painter.setFont(QFont('Arial', fontsize))
        self.painter.drawText(rect, Qt.AlignCenter, str(ws))

    # 画区域
    def drawPolygons(self, points):
        self.painter.setPen(QColor(255, 172, 39))
        self.painter.setBrush(QColor(211, 211, 39))
        self.painter.drawPolygon(QPolygon(points), Qt.WindingFill)

    # 计算坐标
    def calculatePoint(self, angle_old):
        angle = math.radians(angle_old)
        toX = int(((self.width() - 40) / 2 - self.width() / 9) * math.sin(angle) + self.width() / 2)
        toY = int(((self.height() - 40) / 2 - self.height() / 9) * math.cos(angle) * -1 + self.height() / 2)
        fromX = self.width() - toX
        fromY = self.height() - toY
        return fromX, fromY, toX, toY

    # 计算坐标
    def calculatePoint1(self, angle_old):
        angle = math.radians(angle_old)
        toX = int((self.width() / 2 - self.width() / 20) * math.sin(angle) + self.width() / 2)
        toY = int((self.height() / 2 - self.height() / 20) * math.cos(angle) * -1 + self.height() / 2)
        fromX = self.width() - toX
        fromY = self.height() - toY
        return toX, toY, fromX, fromY


# 窗口类
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt5画图类")
        self.resize(500, 500)
        self.setup_ui()

        # 定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.get_wind)
        self.timer.start(3000)

    def setup_ui(self):
        # 子控件加这里
        self.area = PaintArea(self)
        self.area.resize(300, 300)
        self.area.move(100, 100)

    # 随机产生风向风速，动态绘图
    def get_wind(self):
        wind_direction = random.randint(0, 359)
        wind_speed = random.randint(0, 18)
        self.area.setWindDirection(wind_direction)
        self.area.setWindSpeed(wind_speed)
        self.area.update()  # 动态刷新风


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
