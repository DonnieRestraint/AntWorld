from PyQt5.QtCore import Qt
from PyQt5.uic.properties import QtWidgets
from MoonLight import Loader


class YTableWidget(QtWidgets.QTableWidget):
    objectStyle = """
        QTableWidget#TaskTableWidget{
            border:0px;
            margin:0px;
            padding:0px;
            background:rgba(255, 255, 255, 255);
        }
        """

    def __init__(self, parent=None):
        super(YTableWidget, self).__init__(parent)
        self.setObjectName("TaskTableWidget")
        # 允许右键产生菜单
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        # 将右键菜单绑定到槽函数generateMenu
        self.customContextMenuRequested.connect(self.generateMenu)
        self.cols = 3
        Loader.passQss(self)

    def generateMenu(self, pos):
        row_num = -1
        for i in self.selectionModel().selection().indexes():
            row_num = i.row()
            print(row_num)
        if row_num < 2:
            menu = QtWidgets.QMenu()
            item1 = menu.addAction("右键点中了一行")

            action = menu.exec(self.mapToGlobal(pos))
            if action == item1:
                print('第一项', self.item(row_num, 0).text(), self.item(row_num, 1).text(), self.item(row_num, 2).text())

    def update_data(self, data):
        if not data:
            return
        else:
            print(data)
        # count = random.choice(list(range(30)))
        # data = [[(i, j) for j in range(3)] for i in range(count)]
        rows, cols = len(data), self.cols
        self.setRowCount(rows)
        self.setColumnCount(cols)
        # self.setHorizontalHeaderLabels(['bane', 'user', 'code'])
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # self.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.horizontalHeader().hide()
        self.verticalHeader().hide()
        self.setShowGrid(False)  # 关闭网格
        for row in range(rows):
            for col in range(cols):
                new_item = QtWidgets.QTableWidgetItem(str(data[row][col]))
                new_item.setFlags(Qt.ItemIsEnabled)
                new_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置中心对称
                self.setItem(row, col, new_item)
        self.viewport().update()
