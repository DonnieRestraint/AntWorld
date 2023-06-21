"""
https://blog.csdn.net/m0_58086930/article/details/125734826?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-125734826-blog-129162577.235^v36^pc_relevant_default_base3&spm=1001.2101.3001.4242.1&utm_relevant_index=3
MenuBar 上上方菜单栏

NavBarSub上方副导航
DisplayBox中间展示框
TaskBar下方任务按钮

NavBar 左边导航按钮和logo

InfoBox 右上基本信息展示，右下状态信息展示
"""
from PyQt5.QtWidgets import QWidget, QStackedWidget, QVBoxLayout, QApplication

from MoonLight.StyleLoader import Loader
from MoonLight.DynamicWidget.searchPage import SQWidget
from MoonLight.DynamicWidget.yyhPage import YYQWidget


class BrowserWidget(QWidget):
    objectStyle = """
        QStackedWidget#TaskStackedWidget{
            margin:0px;
            padding:0px;
            background: rgba(215,200,200,0);
        }
        """

    def __init__(self, parent=None):
        super(BrowserWidget, self).__init__(parent)
        self.setObjectName("BrowserWidget")
        self.root_parent = parent
        Loader.passQss(self)
        self.initLayout()

    def initLayout(self):
        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setObjectName("TaskStackedWidget")
        Loader.attrAttach(self.stackedWidget)
        # Loader.boundAttach(self.stackedWidget)
        layout = QVBoxLayout()
        layout.addWidget(self.stackedWidget)
        self.setLayout(layout)
        Loader.spaceAttach(layout)
        Loader.boundAttach(layout)
        self.create_page()

    def create_page(self):
        self.stackedWidget.addWidget(SQWidget(self.root_parent))
        self.stackedWidget.addWidget(YYQWidget(self.root_parent))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    demo = BrowserWidget()
    demo.show()
    sys.exit(app.exec_())
