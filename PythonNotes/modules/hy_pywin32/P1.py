import os
import threading
import shutil
import win32com
from win32api import RGB
from win32com import client
MODE_DEV, MODE_PRO = False, True





class ExcelMaker(object):
    """
    A excel operator classAble by win32
    """
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(ExcelMaker, "_instance"):
            with ExcelMaker._instance_lock:
                if not hasattr(ExcelMaker, "_instance"):
                    ExcelMaker._instance = object.__new__(cls)
        return ExcelMaker._instance

    def _get_app(self):
        """
        Dispatch 会试图复用已有的工作薄,
        EnsureDispatch 会创建开发缓存, 试图复用已有的工作薄,
        DispatchEx 会新建一个工作薄

        app = win32com.client.Dispatch('Excel.Application')
        for a in app.Workbooks:
            print(a.Name, a.Path)
        """

        if self.mode == MODE_DEV:
            # 会生成python开发缓存
            return client.gencache.EnsureDispatch(self.app_name)
        else:
            # 不会生成python开发缓存
            return client.DispatchEx(self.app_name)



    def get_app(self):
        """Obtain the excel operator of pywin32 """
        if not self.excel:
            self.excel = self._get_app()
        else:
            return self.excel

        if self.mode == MODE_DEV:
            self.excel.Visible = True
        self.excel.DisplayAlerts = self.alerts
        return self.excel

    def Quit(self):
        try:
            self.excel.Application.Quit()
        except:
            pass

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.Quit()

    def __del__(self):
        if self.mode == MODE_DEV:
            print("Folder Cleared : %s" % win32com.__gen_path__)
            shutil.rmtree(win32com.__gen_path__)

    def __init__(self, mode=MODE_PRO, visible=False, alerts=False):
        self.app_name = "Excel.Application"
        self.mode = mode
        self.visible = visible
        self.alerts = alerts
        self.excel = None


if __name__ == '__main__':
    """
    pywin32调用接口名称可以在打印Folder Cleared的目录路径下的文件进行查看
    建议使用xlwings来操作excel, xlwings是win32com的一个集成 
    import xlwings
    """
    # client.constants.xlEdgeRight
    # xlEdgeRight = client.constants.xlEdgeRight = 10
    # xlThin = client.constants.xlThin = 2
    fp = os.path.abspath("../files/xlmarker.xlsx")
    fp2 = os.path.abspath("../files/xlmarker2.xlsx")
    range_str = "B4:H10"
    range_str2 = "A1:Z3"
    print(os.path.exists(fp))
    print(os.path.exists(fp2))
    with ExcelMaker(False) as em:
        excel = em.get_app()
        wb = excel.Workbooks.Open(fp)
        # 最后一个sheet
        last_ws = wb.Sheets(wb.Sheets.Count)
        # 写入数据
        last_ws.Cells(3, 4).Value = "string"
        # font bg color
        length = len("string")
        last_ws.Cells(3, 4).GetCharacters(1, length).Font.Color = RGB(0, 0, 255)
        last_ws.Cells(3, 4).Interior.Color = RGB(0, 222, 255)

        # 设置颜色
        last_ws.Range(range_str2).Borders.Color = RGB(255, 0, 255)
        # 合并单元格
        last_ws.Range(range_str).Merge()
        #设置边框粗细, 第一个设置成了网格, 第二个是一个range当做整体设置右边框
        # last_ws.Range(range_str).Borders.Weight = 3
        last_ws.Range(range_str).Borders(6).Weight = 3
        last_ws.Range(range_str).Borders(9).Weight = 3
        last_ws.Range(range_str).Borders(7).Weight = 3
        last_ws.Range(range_str).Borders(10).Weight = 3
        # 斜的 up down
        last_ws.Range(range_str).Borders(5).Weight = 3
        last_ws.Range(range_str).Borders(8).Weight = 3
        # 冻结窗口, 选取可用last_ws,也可以用excel,当激活的sheet就是想要冻结的sheet时一样
        last_ws.Activate()
        last_ws.Range("B3").Select()
        excel.ActiveWindow.FreezePanes = False
        excel.ActiveWindow.FreezePanes = True

        # 创建表
        # nws = wb2.Worksheets.Add()
        # 更改表名
        # nws.Name = "Sheet110"
        # 移动句柄至要操作的表
        # wb.Worksheets("Sheet100").Activate()
        # 选择区域, 如果主动移动了句柄, 和当前句柄不一样就会报错
        # wb.Worksheets("Sheet100").Range(range_str).Cells.Select()
        # 工作薄内,此复制表的方式和下一种类似,但不会创建新表, 指定的表名不存在会报错, 需要先移动句柄到要选定区域的表上, 再选定区域或全表
        # excel.Selection.Copy(Destination=wb.Worksheets("Sheet1110").Range(range_str.split(":")[0]))
        # 工作薄内,复制区域, 此方式会在最后一个sheet附近(当前是后面)创建一个唯一的表进行粘贴
        # wb.Worksheets(wb.Sheets.Count-1).Copy(None, wb.Sheets(wb.Sheets.Count))
        # 创建工作薄
        wb2 = excel.Workbooks.Add()
        # # 向其他工作薄复制粘贴区域, 此方式会在最后一个sheet附近(当前是后面)创建一个唯一的表进行粘贴
        wb.Worksheets(wb.Sheets.Count).Copy(None, wb2.Sheets(wb2.Sheets.Count))
        # 故可以改指定索引的表的表名
        new_sheet = wb2.Sheets(wb2.Sheets.Count)
        new_sheet.Name = "Sheet Last"
        # 保存更改
        wb.SaveAs(fp)
        # 关闭excel的特殊状态, 类似打开excel,没有sheet的那种状态, 需要拖入一个xlsx文件才能恢复正常状态
        wb.Close(fp)
        wb2.SaveAs(fp2)
        wb2.Close(fp2)

        # 退出excel
