import sys
from PyQt5.QtCore import Qt, QPoint, pyqtSignal
from PyQt5.QtGui import QMouseEvent, QCursor, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QAction, QMessageBox


class DragWindow(object):
    """drag and drop the window mode"""
    def init_param(self):
        self._isTracking = False
        self._startPos = None
        self._endPos = None

    def mousePressEvent(self, e: QMouseEvent):
        """mouse press"""
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())
        else:
            self._isTracking = False

        if self.isMaximized():
            self.init_param()

    def mouseMoveEvent(self, e: QMouseEvent):
        if self._isTracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self.init_param()


class MainFrame(QMainWindow, DragWindow):
    rightClicked = pyqtSignal([QPoint])

    def __init__(self):
        super(MainFrame, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(400, 300)
        # 右键菜单
        # self.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.customContextMenuRequested.connect(self.showMenu)
        self.rightClicked[QPoint].connect(self.showMenu)
        self._show_menu()

    def mousePressEvent(self, evt):
        super(MainFrame, self).mousePressEvent(evt)
        DragWindow.mousePressEvent(self, evt)
        if evt.button() == Qt.RightButton:
            self.rightClicked[QPoint].emit(evt.pos())

    def rightClick(self, evt):
        print("自定义的右键点击事件")

    def contextMenuEvent(self, evt):
        print("捕捉到右键点击")

    def _show_menu(self):
        self.contextMenu = QMenu(self)
        tree_menu = [
            ("复制", None),
            ("剪切", None),
            ("功能", [("增加", None), ("修改", None), ("删除", None)])
        ]
        if not hasattr(self.contextMenu, "list_menu"):
            setattr(self.contextMenu, "list_menu", list())

        self.add_tree(tree_menu, None)

    def add_tree(self, tree, parent):
        if not tree:
            return
        for menu in tree:
            key, val = menu
            if not val:
                if not parent:
                    parent = self.contextMenu
                #
                sub_menu = parent.addAction(QIcon("favicon.ico"), key)
                self.contextMenu.list_menu.append(sub_menu)
                sub_menu.triggered.connect(self.branchMenuEvent)
            else:
                if not parent:
                    parent = self.contextMenu
                sub_menu = parent.addMenu(key)
                self.contextMenu.list_menu.append(sub_menu)
            self.add_tree(val, sub_menu)

    def showMenu(self, pos):
        print(pos, QCursor.pos())
        # 在鼠标位置显示
        self.contextMenu.exec(QCursor.pos())

    def branchMenuEvent(self):
        # QMessageBox.information(self, "提示：", '   您选择了' + self.sender().text())
        print(self, "提示：", '   您选择了' + self.sender().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainFrame()
    frame.show()
    # from SoftwareInterface.untitled_qrc import Ui_MainWindow
    # ui = Ui_MainWindow()
    # ui.setupUi(frame)
    sys.exit(app.exec())

