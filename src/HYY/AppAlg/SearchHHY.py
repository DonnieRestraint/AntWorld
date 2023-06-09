import os
from pathlib import Path
import re
import time
import concurrent.futures as future_factor
from multiprocessing import cpu_count


class KeySearch(object):
    def __init__(self, root_path, key="YYH"):
        self.key = key
        self.key_path = {}
        self.path_list = []
        self.root_path = root_path
        self.file_filter_regex = ".*(.py|.md|.txt)$"

    def get_path(self):
        # YYH Future的使用进行多线程文件内容搜索
        # 并发: 对应python中的多线程 / 协程, 适用于I/O频繁的操作
        # 并行: 对应python中的多进程, 适用于CPU密集型的操作
        # concurrent.futures模块和asyncio模块 都有一个Future类 其实例表示已经完成或者尚未完成的延迟计算,类似JavaScript中的Promise对象
        workers = cpu_count() * 2 or cpu_count() + 2
        with future_factor.ThreadPoolExecutor(max_workers=workers) as executor:
            todo_list = []
            for path in self.path_list:
                future = executor.submit(self.read_path, path)
                todo_list.append(future)
            for future in future_factor.as_completed(todo_list):
                future.add_done_callback(self.hy_print)
                # running/pending/finished 是future的三种状态
                future.result()

    def hy_print(self, future):
        # 再次查询结果
        # print(future, future.result())
        pass

    def read_path(self, path):
        file_content = []
        path = os.path.abspath(path)
        if len(path) >= 250:
            file_path = "\\\\?\\" + path
        else:
            file_path = path
        if not re.match(self.file_filter_regex, path):
            return path, "-1"
        # print("1", os.stat("\\\\?\\" + path).st_size / 1024)
        # print("2", os.path.getsize("\\\\?\\" + path) / 1024)
        # print("3", Path("\\\\?\\" + path).stat().st_size / 1024)
        size_10m = os.path.getsize("\\\\?\\" + path) > 1024 * 1024
        with open(file_path, "r", encoding="utf-8") as f:
            if not size_10m:
                for line_y in f.readlines():
                    if self.regex_search(line_y):
                        file_content.append(line_y)
            else:
                line_y = f.readline()
                while line_y:
                    if self.regex_search(line_y):
                        file_content.append(line_y)
                    line_y = f.readline()
        if file_content:
            self.key_path.update({path: file_content})
        return path

    def regex_search(self, string):
        result = re.search(self.key, string, re.I)
        if result:
            return True
        else:
            return False

    def iter_root_path(self):
        if os.path.exists(self.root_path) and os.path.isdir(self.root_path):
            for dir_path, dir_name, files_name in os.walk(self.root_path):
                for file_name in files_name:
                    file_path = os.path.join(dir_path, file_name)
                    self.path_list.append(file_path)
        else:
            self.read_path(self.root_path)

    def main(self):
        start = time.time()
        self.iter_root_path()
        self.get_path()
        take = time.time() - start
        print(self.key_path)
        return f"search using {'%.02f' % take}s"


if __name__ == '__main__':
    p = Path(r'\foo')
    print(Path(r'\foo') / 'bar')
    KeySearch(r"D:\Donnie\Notes\AntNotes\PythonNotes\modules").main()
