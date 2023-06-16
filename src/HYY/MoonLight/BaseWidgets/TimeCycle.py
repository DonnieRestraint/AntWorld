from PyQt5.Qt import *
from datetime import datetime, time

from AppAlgorithm.UserConfig import UserConfig


class DateTimeEdit(QDateTimeEdit):
    setStyle = """
    QDateTimeEdit#anchorTime{
        background-color: rgb(67, 60, 58, 255);
        border: 2px solid rgba(67, 60, 58, 255);
        border-radius:0px;
        font-size: 18px;
        font-weight: 400;
        font-family:monospace;
        color: rgba(118, 101, 85, 255);
        selection-color: rgba(51, 51, 51, 1);
        selection-background-color: rgba(118, 101, 85, 1);
    }
    """

    timer_name = "Timer"
    timer_sub_name = "anchor_time"
    dt_strftime = "%Y-%m-%d %H:%M:%S"
    qt_strftime = "yyyy-MM-dd HH:mm:ss"

    def __init__(self, parent=None):
        anchor_time = self.get_anchorTime()
        if not anchor_time:
            qt_datetime = QDateTime.currentDateTime()
        else:
            qt_datetime = QDateTime(datetime.strptime(anchor_time, self.dt_strftime))

        super().__init__(qt_datetime, parent=parent)  # 设置控件(大小、位置、样式...)
        self.setObjectName("anchorTime")

        self.current_datetime = datetime.strftime(qt_datetime.toPyDateTime(), self.dt_strftime)
        self.setDisplayFormat(self.qt_strftime)
        self.setStyleSheet(self.setStyle)
        # 设置最小日期
        # self.setMinimumDate(QDate.currentDate().addDays(-365))
        # 设置最大日期
        # self.setMaximumDate(QDate.currentDate().addDays(365))
        # True，弹出日历控件
        self.setCalendarPopup(False)
        # 建立信号与相应槽的连接
        self.dateChanged.connect(self.onDateChanged)
        self.dateTimeChanged.connect(self.onDateTimeChanged)
        self.timeChanged.connect(self.onTimeChanged)
        # self.editingFinished.connect(self.onEditingFinished)

    def onDateChanged(self, qt_date):
        # 无论日期还是时间发生改变，都会执行
        # print("onDateChanged", qt_date)
        ...

    def onDateTimeChanged(self, qt_datetime):
        # 时间发生改变时执行
        self.current_datetime = datetime.strftime(qt_datetime.toPyDateTime(), self.dt_strftime)
        # print("onDateTimeChanged", qt_datetime)

    def onTimeChanged(self, qt_time):
        # print("onTimeChanged", qt_time)
        ...

    def get_anchorTime(self):
        uc = UserConfig()
        config = uc.read_config()
        if not config:
            return 
        for section in config.sections():
            options = config.options(section)
            for option in options:
                if section == self.timer_name and option == self.timer_sub_name:
                    return config.get(section, option)

    def on_BeSure_clicked(self, e):
        uc = UserConfig()
        uc.write(Timer={self.timer_sub_name: self.current_datetime})
        # config = uc.read_config()
        # uc.check_config(config)


if __name__ == '__main__':
    import sys

    # 1、创建一个应用程序对象
    app = QApplication(sys.argv)
    # 2、控件的操作    #创建控件
    demo = DateTimeEdit()
    # 展示控件
    demo.show()
    # 3、应用程序的执行，进入到消息循环
    sys.exit(app.exec_())
