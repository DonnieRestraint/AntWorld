import os
import time
import psutil
import datetime
import threading
import collections
import numpy as np
import pandas as pd
import xlwings as xw
import multiprocessing
from pathlib import Path
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plot


class ExcelMarker(object):

    def __init__(self, visible=False, add_book=False):
        self.pid_name = "excel.exe"
        self.opened_excel_pid = xw.apps.keys()
        self.app = xw.App(visible=visible, add_book=add_book)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.app.quit()


    def demo_one(self):
        pass


def demo_zero():
    print(Path(__file__))
    name = "xlmarker.xlsx"
    file_name = os.path.abspath("../files/xlmarker.xlsx")
    wb = xw.Book()
    ws = wb.sheets[1]
    ws["A1"].value = 23
    wb.save()
    wb.close()






if __name__ == '__main__':
    fp = os.path.abspath("../files/xlmarker.xlsx")
    fp2 = os.path.abspath("../files/xlmarker2.xlsx")
    demo_zero()

    # app = xw.App(visible=False, add_book=False)
    #
    # workbook = app.books.open(fp)
    # workbook2 = app.books.open(fp2)
    # # print(workbook.sheets["Sheet Last"].name)
    # worksheet = workbook.sheets[0]
    # print(worksheet.name)
    # print(worksheet["D3"].value)
    # worksheet['A1'].value = "ABC"
    # # worksheet2 = workbook.sheets[1]
    # # print(worksheet.range("D3").value)
    # worksheet.range("A1:I12").copy(workbook2.sheets[0].range("A1:I12"))
    # workbook.save()
    # workbook.close()
    # workbook2.save()
    # workbook2.close()
    # app.quit()
    # # book = xw.Book(fp)
    # # sheet = book.sheets[0].copy("report")
    # # book.save()
    # # book.close()
    #


