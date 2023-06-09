from PyQt5.Qt import *


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

    def __init__(self, parent=None, datetime=QDateTime.currentDateTime()):
        super().__init__(datetime, parent=parent)  # 设置控件(大小、位置、样式...)
        self.setObjectName("anchorTime")
        self.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
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

    def onDateChanged(self, date):
        # 无论日期还是时间发生改变，都会执行
        print("onDateChanged", date)

    def onDateTimeChanged(self, dateTime):
        # 时间发生改变时执行
        print("onDateTimeChanged",dateTime)

    def onTimeChanged(self, time):
        print("onTimeChanged",time)

    def onBeSure(self):
        print("read go")

    def onEditingFinished(self):
        dateTime = self.dateTime()
        # 最大日期
        maxDate = self.maximumDate()
        # 最大日期时间
        maxDateTime = self.maximumDateTime()
        # 最大时间
        maxTime = self.maximumTime()
        # 最小日期
        minDate = self.minimumDate()
        # 最小日期时间
        minDateTime = self.minimumDateTime()
        # 最小时间
        minTime = self.minimumTime()
        print('\n选择日期时间')
        print('dateTime=%s' % str(dateTime))
        print('maxDate=%s' % str(maxDate))
        print('maxDateTime=%s' % str(maxDateTime))
        print('maxTime=%s' % str(maxTime))
        print('minDate=%s' % str(minDate))
        print('minDateTime=%s' % str(minDateTime))
        print('minTime=%s' % str(minTime))


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
