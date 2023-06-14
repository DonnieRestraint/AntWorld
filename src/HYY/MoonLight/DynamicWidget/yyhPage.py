import math
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut, QLabel

from AppAlgorithm.Solve import Solve
from MoonLight.StyleLoader import Loader

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import Qt, pyqtSignal
from MoonLight.BaseWidgets.LineEdit import LineEdit
import os


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
        rows, cols = len(data), 3
        self.setRowCount(rows)
        self.setColumnCount(cols)
        self.setHorizontalHeaderLabels(['bane', 'user', 'code'])
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


class YYQWidget(QtWidgets.QWidget):
    dataSignal = pyqtSignal(object)
    style = """
            QLineEdit#filePath {
                padding:0px;
                margin:5px 5px 5px 5px;
            
                background-color: rgba%(white)s;
                color:rgba(143,143,143,255);
            
                border: 0px solid grey;
                border-radius:0px;
            
                font-size: 14px;
                font-weight: %(font_bold)s;
                font-family:%(font_family)s;
            }
            QLineEdit#saltInput {
                padding:0px;
                margin:5px 5px 5px 5px;
            
                background-color: rgba%(white)s;
                color:rgba(143,143,143,255);
            
                border: 0px solid grey;
                border-radius:0px;
                font-size: 14px;
                font-weight: %(font_bold)s;
                font-family:%(font_family)s;
            }
            QPushButton#runButton{
                padding:0px;
                margin:5px 5px 5px 5px;
                background-color: rgba%(white)s;
                color:rgba(143,143,143,255);
            
                border: 0px solid grey;
                border-radius:5px;
            
                font-size: 14px;
                font-weight: %(font_bold)s;
                font-family:%(font_family)s;
            }
            QWidget#tipLabel{
                font-size: 20px;
                font-weight: 400;
                font-family: monospace;
            }
            """

    def __init__(self, parent=None):
        super(YYQWidget, self).__init__(parent)
        self.pro_yyh = "YYH_"
        # 隐藏窗口
        self.root_parent = parent
        Loader.passQss(self)
        self.setTaskPushButton()

    def setTaskPushButton(self):
        self.tableWidget = YTableWidget(self)
        self.tableWidget.viewport().installEventFilter(self.root_parent)
        Loader.attrAttach(self.tableWidget)


        self.ontologyPath = LineEdit(self)
        self.ontologyPath.setPlaceholderText("Ontology Path")
        self.ontologyPath.setObjectName("filePath")

        self.appendPath = LineEdit(self)
        self.appendPath.setPlaceholderText("Append Path")
        self.appendPath.setObjectName("filePath")

        self.saltInput = LineEdit(self)
        self.saltInput.setPlaceholderText("Code")
        self.saltInput.setObjectName("saltInput")
        self.saltInput.setEchoMode(QtWidgets.QLineEdit.Password)
        # self.saltInput.returnPressed.connect(self.task_handle_button)
        # 小enter, 大enter
        QShortcut(QKeySequence("Enter"), self.saltInput, self.task_handle_button)
        QShortcut(QKeySequence("Return"), self.saltInput, self.task_handle_button)

        self.runButton = QtWidgets.QPushButton("go", self)
        self.runButton.clicked[bool].connect(self.task_handle_button)
        self.runButton.setCheckable(True)
        self.runButton.setObjectName("runButton")

        self.tipLabel = QLabel(self)
        self.tipLabel.setObjectName("tipLabel")
        self.tipLabel.setText("......")
        # Loader.attrAttach(self.tipLabel)

    def handle_data(self, args):
        salts = args[2]
        mid = math.ceil(len(salts) / 2)
        salt = salts[:mid]
        salt_ = salts[mid:]

        if not (len(salt) - len(salt_) == 0 and salt == salt_[::-1] or len(salt) - len(salt_) == 1 and salt[:-1] == salt_[::-1] or len(salt) < 16):
            self.task_handle_label("Salt is mistake")
            return
        if args[1].startswith("sql:"):
            print()

        if not os.path.exists(args[0]) and not os.path.exists(args[1]):
            self.task_handle_label("Please input file path.")
        sl = Solve()
        second_encode_data = None
        if os.path.exists(args[1]):
            second_path = os.path.abspath(args[1])
            rl = sl.check_file(second_path)
            if not rl:
                second_encode_data = sl.file_to_encode(sl.get_file_data(second_path), salt)
            else:
                second_encode_data = sl.get_file_data(second_path)
            rl_salt = sl.check_data_salt(second_encode_data, salt)
            if rl_salt:
                self.task_handle_label("Append Path 数据已获取")
            else:
                self.task_handle_label("Append Path and Salt do not match")
                return None
        if os.path.exists(args[0]):
            first_path = os.path.abspath(args[0])
            if os.path.exists(first_path):
                rl = sl.check_file(first_path)
                if not rl:
                    first_encode_data = sl.file_to_encode(sl.get_file_data(first_path), salt)
                else:
                    first_encode_data = sl.get_file_data(first_path)
                rl_salt = sl.check_data_salt(first_encode_data, salt)
                if rl_salt:
                    self.task_handle_label("The Ontology Data has been obtained")
                else:
                    self.task_handle_label("Ontology Data and Salt do not match")
                    return None
                first_encode_data = sl.map_data([first_encode_data, second_encode_data]) if second_encode_data else first_encode_data
                dir_name, base_name = os.path.dirname(first_path), os.path.basename(first_path)
                rl_salt = sl.check_data_salt(first_encode_data, salt)
                if rl_salt:
                    if base_name.startswith(self.pro_yyh):
                        to_path = first_path
                    else:
                        to_path = os.path.join(dir_name, "YYH_" + base_name)
                    sl.set_file_data(to_path, first_encode_data, mode="w")
                    return sl.file_to_decode(first_encode_data, salt)
                else:
                    self.task_handle_label("Salt not match")
        else:
            if second_encode_data:
                second_path = os.path.abspath(args[1])
                dir_name, base_name = os.path.dirname(second_path), os.path.basename(second_path)
                if base_name.startswith(self.pro_yyh):
                    to_path = second_path
                else:
                    to_path = os.path.join(dir_name, "YYH_" + base_name)
                sl.set_file_data(to_path, str(second_encode_data))
                return sl.file_to_decode(second_encode_data, salt)

    def task_handle_label(self, text):
        self.tipLabel.setText(text)

    def task_handle_button(self):
        args = [self.ontologyPath.text(), self.appendPath.text(), self.saltInput.text()]
        func = self.tableWidget.update_data
        button = self.runButton
        data = None

        try:
            data = self.handle_data(args)
        except Exception as err:
            self.task_handle_label("Fail")
        finally:
            button.setEnabled(True)

        if data is None:
            return
        self.dataSignal[object].connect(func)
        self.dataSignal[object].emit(data)
        self.dataSignal[object].disconnect(func)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        width, height = self.width(), self.height()
        step = 0.05
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, self.Int(width, 1), self.Int(height, 0.93)))
        self.ontologyPath.setGeometry(QtCore.QRect(self.Int(width, step), self.Int(height, 0.937), self.Int(width, 0.2), self.Int(height, 0.06)))
        self.appendPath.setGeometry(QtCore.QRect(self.Int(width, step*2 + 0.2), self.Int(height, 0.937), self.Int(width, 0.2), self.Int(height, 0.06)))
        self.saltInput.setGeometry(QtCore.QRect(self.Int(width, step*3 + 0.2 * 2), self.Int(height, 0.937), self.Int(width, 0.1), self.Int(height, 0.06)))
        self.runButton.setGeometry(QtCore.QRect(self.Int(width, step*4 + 0.2*2 + 0.1), self.Int(height, 0.937), self.Int(width, 0.04), self.Int(height, 0.06)))
        self.tipLabel.setGeometry(QtCore.QRect(self.Int(width, step*5 + 0.2*2 + 0.1 + 0.04), self.Int(height, 0.937), self.Int(width, 0.3), self.Int(height, 0.06)))

    def Int(self, length, ratio):
        return int(length * ratio)
