from PyQt5.QtCore import pyqtSignal
from PyQt5.uic.properties import QtWidgets

from MoonLight import Loader
from MoonLight.BaseWidgets.LineEdits import LineEdit
from MoonLight.BaseWidgets.TableWdigets import YTableWidget


class SQWidget(QtWidgets.QWidget):
    dataSignal = pyqtSignal(object)
    style = """
    
        """

    def __init__(self, parent=None):
        self.root_parent = parent
        Loader.passQss(self)
        self.get_type()

    def get_type(self):
        default = "local"
        if default:
            return default
        else:
            return "online"

    def setup_layout(self):
        self.tableWidget = YTableWidget(self)
        self.tableWidget.viewport().installEventFilter(self.root_parent)
        Loader.attrAttach(self.tableWidget)

        self.urlPath  = LineEdit(self)
        self.urlPath.setPlaceholderText("")
        self.urlPath.setObjectName("urlPath")

        self.typeButton