import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QTranslator
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, \
    QComboBox, QVBoxLayout, QMainWindow


class Demo(QWidget):
    def setupUi(self, Form):
        self.button = QPushButton(Form)
        self.label = QLabel(Form)
        self.label.setAlignment(Qt.AlignCenter)
        self.combo = QComboBox(Form)
        self.combo.addItem('English')
        self.combo.addItem('中文')
        self.combo.addItem('français')

        self.combo.setGeometry(QtCore.QRect(0, 0, 60, 23))
        self.button.setGeometry(QtCore.QRect(0, 22, 60, 23))
        self.label.setGeometry(QtCore.QRect(0, 44, 60, 23))
        self.retranslateUi()

    def retranslateUi(self):
        self.button.setText(QApplication.translate('Demo', 'Start'))
        self.label.setText(QApplication.translate('Demo', 'Hello, World'))


class Tables(QMainWindow, Demo):
    def __init__(self, parent=None):
        super(Tables, self).__init__(parent)
        self.setupUi(self)
        self.combo.currentTextChanged.connect(self.change_func)
        self.trans = QTranslator(self)

    def change_func(self):

        if self.combo.currentText() == '中文':
            self.trans.load('eng-chs')
            _app = QApplication.instance()
            _app.installTranslator(self.trans)

        elif self.combo.currentText() == 'français':
            self.trans.load('eng-fr')
            _app = QApplication.instance()
            _app.installTranslator(self.trans)

        else:
            _app = QApplication.instance()
            _app.removeTranslator(self.trans)
        self.retranslateUi()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Tables()
    demo.show()
    sys.exit(app.exec_())