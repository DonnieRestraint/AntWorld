import os
import re
from queue import Queue

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import pyqtSignal, QThread, QTimer
from PyQt5.QtWidgets import QRadioButton, QLabel, QHBoxLayout, QWidget
import concurrent.futures as future_factor
from multiprocessing import cpu_count
from AppAlgorithm.SearchHHY import KeySearch
from MoonLight import Loader
from MoonLight.BaseWidgets.LineEdits import LineEdit
from MoonLight.BaseWidgets.TableWdigets import YTableWidget


class SQWidget(QWidget):
    dataSignal = pyqtSignal(object)
    objectStyle = """
        QWidget#SearchWidget{
            background:grey;
        }
        QLineEdit#urlPath {
            padding:0px;
            margin:5px 5px 5px 5px;
        
            background-color: rgba%(white)s;
            color:rgba(143,143,143,255);
        
            border: 0px solid grey;
            border-radius:0px;
            indent:20px;
            font-size: 14px;
            font-weight: %(font_bold)s;
            font-family:%(font_family)s;
        }
        QLineEdit#keyInput {
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
        QWidget#labelName{
            font-size: 16px;
            font-weight: 700;
            font-family: monospace;
            color:rgba(143,143,143,255);
        }
        QWidget#tipLabel{
            font-size: 20px;
            font-weight: 400;
            font-family: monospace;
            color:rgba(143,143,143,255);
        }
        """

    def __init__(self, parent=None):
        super(SQWidget, self).__init__(parent)
        self.root_parent = parent
        self.setObjectName("SearchWidget")
        self.setup_layout()
        Loader.passQss(self)

    def setup_layout(self):
        self.tableWidget = YTableWidget(self)
        self.tableWidget.viewport().installEventFilter(self.root_parent)
        Loader.attrAttach(self.tableWidget)

        self.urlPath  = LineEdit(self, file_type="dir")
        self.urlPath.setPlaceholderText("UrlPath")
        self.urlPath.setObjectName("urlPath")

        self.KeyInput  = LineEdit(self)
        self.KeyInput.setPlaceholderText("KeySearch")
        self.KeyInput.setObjectName("keyInput")
        self.KeyInput.returnPressed.connect(self.OnClickedSearch)
        self.read_type = QWidget(self)
        h1_layout = QHBoxLayout()
        self.read_type.setLayout(h1_layout)
        self.read_loader_point = FileSearch.file_type
        self.read_label1 = QLabel(self.read_loader_point[0], self.read_type)
        self.read_label1.setObjectName("labelName")
        self.read_is = QRadioButton(self.read_type)
        self.read_not = QRadioButton(self.read_type)
        self.read_is.toggled.connect(lambda isChecked: self.switch_file_type(isChecked))
        self.read_is.setChecked(True)
        h1_layout.addWidget(self.read_is)
        h1_layout.addWidget(self.read_not)
        h1_layout.addWidget(self.read_label1)
        Loader.boundAttach(self.read_type, (50, 0, 0, 0))
        Loader.spaceAttach(h1_layout)

        self.loader_type = QWidget(self)
        h2_layout = QHBoxLayout()
        self.loader_type.setLayout(h2_layout)
        self.read_loader_pass = FileSearch.load_type
        self.read_label2 = QLabel(self.read_loader_pass[0], self.loader_type)
        self.read_label2.setObjectName("labelName")
        self.read_local = QRadioButton(self.loader_type)
        self.read_local.toggled.connect(lambda isChecked: self.switch_load_type(isChecked))
        self.read_local.setChecked(True)
        self.read_online = QRadioButton(self.loader_type)
        h2_layout.addWidget(self.read_local)
        h2_layout.addWidget(self.read_online)
        h2_layout.addWidget(self.read_label2)
        Loader.boundAttach(self.loader_type, (50, 0, 0, 0))
        Loader.spaceAttach(h2_layout)

        self.tipLabel = QLabel(self)
        self.tipLabel.setObjectName("tipLabel")
        self.tipLabel.setText("...")

    def task_handle_label(self, text):
        self.tipLabel.setText(text)

    def Int(self, length, ratio):
        return int(length * ratio)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        width, height = self.width(), self.height()
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, width, self.Int(height, 0.8)))
        self.urlPath.setGeometry(QtCore.QRect(self.Int(width, 0.05), self.Int(height, 0.86), self.Int(width, 0.6), self.Int(height, 0.07)))
        self.KeyInput.setGeometry(QtCore.QRect(self.Int(width, 0.7), self.Int(height, 0.86), self.Int(width, 0.25), self.Int(height, 0.07)))
        self.read_type.setGeometry(QtCore.QRect(self.Int(width, 0.05), self.Int(height, 0.93), self.Int(width, 0.2), self.Int(height, 0.07)))
        self.loader_type.setGeometry(QtCore.QRect(self.Int(width, 0.3), self.Int(height, 0.93), self.Int(width, 0.2), self.Int(height, 0.07)))
        self.tipLabel.setGeometry(QtCore.QRect(self.Int(width, 0.6), self.Int(height, 0.93), self.Int(width, 0.3), self.Int(height, 0.07)))

    def switch_file_type(self, e):
        if e:
            self.read_label1.setText(self.read_loader_point[0])
        else:
            self.read_label1.setText(self.read_loader_point[1])

    def switch_load_type(self, e):
        if e:
            self.read_label2.setText(self.read_loader_pass[0])
        else:
            self.read_label2.setText(self.read_loader_pass[1])

    def OnClickedSearch(self):
        filePath = self.urlPath.text()
        keySearch = self.KeyInput.text()
        file_match = self.read_label1.text()
        url_match = self.read_label2.text()
        if self.read_label2.text() == self.read_loader_pass[0]:
            if keySearch:
                ks = FileSearch(filePath, self)
                ks.f_file_type = file_match
                ks.f_load_type = url_match
            else:
                ks = FileSearch(filePath, self)
                ks.f_file_type = file_match
                ks.f_load_type = url_match
            ks.data_signal[dict].connect(self.tableWidget.update_table)
            ks.start()


class FileSearch(QThread):
    file_type = ("FileContent", "FileName")
    load_type = ("Offline", "Online")
    data_signal = pyqtSignal(object)

    def __init__(self, root_url, parent=None):
        super(FileSearch, self).__init__(parent)
        self.parent = parent
        self.regex_key = "hhy"
        self.file_filter_regex = ".*(.py|.md|.txt)$"
        self.file_path_list = []
        self.src_url_list = []
        self.root_url = root_url
        self.f_file_type = self.file_type[0]
        self.f_load_type = self.load_type[0]
        self.data_queue = Queue()
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_emit)
        self.timer.start(1000)

    def run(self) -> None:
        if self.f_load_type == self.load_type[0]:
            self.get_path_list()
        else:
            self.get_url_list()
        self._map_task()

    def _map_task(self):
        # YYH Future的使用进行多线程文件内容搜索
        # 并发: 对应python中的多线程 / 协程, 适用于I/O频繁的操作
        # 并行: 对应python中的多进程, 适用于CPU密集型的操作
        # concurrent.futures模块和asyncio模块 都有一个Future类 其实例表示已经完成或者尚未完成的延迟计算,类似JavaScript中的Promise对象
        workers = cpu_count() * 1
        with future_factor.ThreadPoolExecutor(max_workers=workers) as executor:
            task_list = self.file_path_list if self.f_load_type == self.load_type[0] else self.src_url_list

            todo_list = []
            for task in task_list:
                if self.f_load_type == self.load_type[0]:
                    future = executor.submit(self._match_file, task)
                else:
                    future = executor.submit(self._match_url, task)
                todo_list.append(future)

            for future in future_factor.as_completed(todo_list):
                future.add_done_callback(self._get_task)
                # running/pending/finished 是future的三种状态
                future.result()

    def _exe_task(self):
        pass

    def _get_task(self, future):
        print(future.result())
        data = future.result()
        if data:
            self.data_queue.put(data)

    def get_path_list(self):
        if os.path.exists(self.root_url) and os.path.isdir(self.root_url):
            for dir_path, dir_name, files_name in os.walk(self.root_url):
                for file_name in files_name:
                    file_path = os.path.join(dir_path, file_name)
                    self.file_path_list.append(file_path)

    def regex_search(self, string, regex_key):
        result = re.search(regex_key, string, re.I)
        if result:
            return True
        else:
            return False

    def _match_file(self, path):
        abs_path = os.path.abspath(path)
        base_name = os.path.basename(path)
        if self.f_file_type == self.file_type[1]:
            if self.regex_search(base_name, self.regex_key):
                return {abs_path: [base_name]}
            else:
                return {}
        else:
            # self.file_type[0]
            if len(path) >= 250:
                file_path = "\\\\?\\" + path
            else:
                file_path = path
            if not re.match(self.file_filter_regex, file_path):
                return {}
            size_10m = os.path.getsize(file_path) > 1024 * 1024
            file_content = []
            with open(file_path, "r", encoding="utf-8") as f:
                if not size_10m:
                    for line_y in f.readlines():
                        if self.regex_search(line_y, self.regex_key):
                            file_content.append(line_y)
                else:
                    line_y = f.readline()
                    while line_y:
                        if self.regex_search(line_y, self.regex_key):
                            file_content.append(line_y)
                        line_y = f.readline()
            if file_content:
                return {path: file_content}
            else:
                return {}

    def timer_emit(self):
        # print(self.data_queue.qsize())
        if self.data_queue.qsize():
            data_dict = {}
            while self.data_queue.qsize():
                d_dict = self.data_queue.get()
                for k, d in d_dict.items():
                    if k not in data_dict:
                        data_dict[k] = d
                    else:
                        if isinstance(d, (list, tuple)):
                            [data_dict[k].append(content) for content in d]
                        else:
                            data_dict[k] = d
            self.data_signal.emit(data_dict)

    def get_url_list(self):
        pass

    def _match_url(self, url):
        pass
