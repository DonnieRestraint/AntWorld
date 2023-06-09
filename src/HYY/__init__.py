import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QScrollBar, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('ScrollBar Demo')
        self.bt = QPushButton("Sdf", self)
        self.scrollbar = QScrollBar(Qt.Vertical, self)
        self.scrollbar.setGeometry(280, 30, 20, 150)

        # 设置滑块位置为50
        self.scrollbar.setValue(50)
        self.scrollbar.valueChanged.connect(self.pprint)

    def pprint(self, val):
        print(val)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())