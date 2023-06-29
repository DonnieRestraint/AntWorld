from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from pathlib import Path
import platform


class HYLineEdit(QLineEdit):

    def __init__(self, parent=None, hy_only_type=None):
        super(HYLineEdit, self).__init__(parent)        
        self.setAcceptDrops(True)
        self.hy_only_type = hy_only_type

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super(HYLineEdit, self).dragEnterEvent(event)

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                if platform.system().startswith("Win"):
                    path = url.path()[1:]
                    self.setValue(path)
                else:
                    self.setText(url.path())
        else:
            super(HYLineEdit, self).dropEvent(event)

    def setValue(self, path):
        if self.hy_only_type == "file" and Path(path).is_file():
            self.setText(path)
        elif self.hy_only_type == "dir" and Path(path).is_dir():
            self.setText(path)
        else:
            if not self.hy_only_type:
                self.setText(path)