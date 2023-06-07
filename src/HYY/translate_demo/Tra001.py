import sys
from PyQt5.QtCore import Qt, QTranslator
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton(self.tr('Start'), self)   # 1
        self.label = QLabel(self.tr('Hello, World'), self)
        self.label.setAlignment(Qt.AlignCenter)
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.button)
        self.v_layout.addWidget(self.label)
        self.setLayout(self.v_layout)


if __name__ == '__main__':
    """
    pylupdate5 main.py  -ts eng-chs.ts
    pylupdate5 main.py  -ts eng-fr.ts
    lrelease eng-fr.ts eng-chs.ts
    """
    app = QApplication(sys.argv)
    trans = QTranslator(app)
    trans.load('eng-chs')
    app.installTranslator(trans)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())