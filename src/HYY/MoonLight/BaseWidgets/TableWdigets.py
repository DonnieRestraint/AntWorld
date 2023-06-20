import collections

from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from MoonLight import Loader


class YTableWidget(QtWidgets.QTableWidget):
    objectStyle = """
        QTableWidget#TaskTableWidget{
            border:0px;
            margin:0px;
            padding:0px;
            background:rgba(255, 255, 255, 255);
            outline:1 solid rgba(91, 87, 78);
        }
        QTableWidget::item{
            color:rgb(118, 101, 91);
            padding:1px;
            background:rgba(240, 255, 250, 255);

            border-bottom: 1 solid rgba(91, 87, 78);
        }
        """

    def __init__(self, parent=None):
        super(YTableWidget, self).__init__(parent)
        self.setObjectName("TaskTableWidget")
        # 允许右键产生菜单
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        # 将右键菜单绑定到槽函数generateMenu
        # self.customContextMenuRequested.connect(self.generateMenu)
        self.cols = 3
        Loader.passQss(self)
        self.setStyleSheet(self.objectStyle)

        # self.setHorizontalHeaderLabels(['bane', 'user', 'code'])
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # self.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.horizontalHeader().hide()
        self.verticalHeader().hide()
        self.setShowGrid(False)  # 关闭网格

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
        rows, cols = len(data), self.cols
        self.setRowCount(rows)
        self.setColumnCount(cols)
        for row in range(rows):
            for col in range(cols):
                new_item = QtWidgets.QTableWidgetItem(str(data[row][col]))
                new_item.setFlags(Qt.ItemIsEnabled)
                new_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置中心对称
                self.setItem(row, col, new_item)
        self.viewport().update()

    def update_table(self, new_data_dict):
        if not new_data_dict:
            return
        else:
            print(new_data_dict)
        data_dict, rows, columns = self.get_table_data()
        whole_rows = rows
        for k, v in new_data_dict.items():
            if v:
                whole_rows = whole_rows + len(v)

        key_list = list(data_dict.keys())
        for k in new_data_dict.keys():
            if k not in key_list:
                key_list.append(k)

        for k in key_list:
            if k in new_data_dict:
                if k in data_dict:
                    pass
                else:
                    data_dict[k] = []
                data_list = data_dict[k]
                for n_d in new_data_dict[k]:
                    cell = n_d.strip()
                    if n_d not in data_list:
                        data_dict[k].append(cell)

        self.setRowCount(whole_rows)
        self.setColumnCount(self.cols - 1)
        row = 0
        for key, val_list in data_dict.items():
            key_item = QtWidgets.QTableWidgetItem(str(key))
            key_item.setFlags(Qt.ItemIsEnabled)
            key_item.setTextAlignment(Qt.AlignCenter)  # 设置中心对称
            self.setItem(row, 0, key_item)
            for ri, val in enumerate(val_list):
                if ri:
                    empty_item = QtWidgets.QTableWidgetItem(str(""))

                    empty_item.setFlags(Qt.ItemIsEnabled)
                    self.setItem(row, 0, empty_item)
                val_item = QtWidgets.QTableWidgetItem(str(val))
                val_item.setFlags(Qt.ItemIsEnabled)
                val_item.setTextAlignment(Qt.AlignCenter)  # 设置中心对称 有\n特殊字符时会造成对齐不生效的假象
                self.setItem(row, 1, val_item)
                print(row, 1, val, val_item.textAlignment())
                row = row + 1
        self.setRowCount(row)
        self.viewport().update()

    def get_table_data(self):
        row = self.currentRow()
        rows = self.rowCount()
        columns = self.columnCount()
        data_dict = collections.OrderedDict()
        kk = ''
        for ri in range(rows):
            row_list = []
            for ci in range(columns):
                item = self.item(ri, ci)
                if item:
                    row_list.append(item.text())
                else:
                    row_list.append("")
            if row_list[0] not in data_dict:
                data_dict[row_list[0]] = row_list[1:]
            else:
                data_dict[row_list[0]].extend(row_list[1:])
        return data_dict, rows, columns
