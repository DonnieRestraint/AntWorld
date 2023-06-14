import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QLineEdit, QFileDialog


class LineEdit(QLineEdit):
    def __init__(self, parent=None, file_type="file"):
        super(LineEdit, self).__init__(parent)
        self.file_type = file_type
        self.setAcceptDrops(True)
        self.file_list = []

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super(LineEdit, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        super(LineEdit, self).dragMoveEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                if self.file_type == "file":
                    if self and str(url.path()[1:]).endswith('.txt'):
                        self.setText(str(url.path()[1:]))

                else:
                    if os.path.isdir(str(url.path()[1:])):
                        self.setText(str(url.path()[1:]))
        else:
            super(LineEdit, self).dropEvent(event)

    def mouseDoubleClickEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            if self.file_type == "file":
                filename, _ = QFileDialog.getOpenFileName(self, 'Open File', '*.txt')
                self.setText(str(filename))
            else:
                filename = QFileDialog.getExistingDirectory(self, 'Open FileUrl', './')
                self.setText(str(filename))
