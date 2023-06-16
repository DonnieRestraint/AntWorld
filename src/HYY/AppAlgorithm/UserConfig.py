import calendar
import configparser
import os
import time
import datetime
import pytz


class UserConfig(object):
    def __init__(self):
        self.home_path = os.path.expanduser('~')
        self.config_name = "yyq.ini"
        self.config_path = os.path.join(self.home_path, self.config_name)
        self.code = "utf-8"
        # print(self.config_path)

    def read_config(self):
        if self.config_name in os.listdir(self.home_path):
            config = configparser.ConfigParser()
            config.read(self.config_path, encoding=self.code)
            return config

    def write(self, **kwargs):
        if self.config_name in os.listdir(self.home_path):
            config = self.read_config()
            if not config:
                config = configparser.ConfigParser()
        else:
            config = configparser.ConfigParser()

        # 查询所有的sections
        exist_key = config.sections()
        for key_d, val_d in kwargs.items():
            if key_d not in exist_key:
                # 添加新的section
                config.add_section(key_d)
            for k, v in val_d.items():
                # 对section下进行写入或更新option和值
                config.set(key_d, k, v)
        # config.write(open(self.config_path, "w", encoding=self.code))
        with open(self.config_path, "w", encoding=self.code) as file:
            config.write(file)

    def check_config(self, config):
        section_option_val = {}
        # 以列表形式返回所有的节点 section
        sections = config.sections()
        # print(sections)
        for section in sections:
            section_option_val[section] = {}
            # 得到指定section的所有选项 option
            options = config.options(section)
            for option in options:
                section_option_val[section][option] = ''
            # 得到指定section的所有键值对
            for option, val in config.items(section):
                section_option_val[section][option] = val
            for option in options:
                # 指定section，option读取值
                val = config.get(section, option)
                print(section, option, val)

    def timestamp_format(self, timestamp):

        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

    def timestamp_offset_format(self, timestamp):
        # gmtime() 函数将一个时间戳转换为UTC时区（0时区）的struct_time, 参数sec表示从1970-1-1以来的秒数
        return time.strftime("%H:%M:%S", time.gmtime(timestamp))

    def get_timestamp(self, weeks=0, days=0, hours=0, minutes=0, seconds=0):
        timedelta_obj = datetime.timedelta(weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds)
        return timedelta_obj

    def get_datetime(self, year=1970, month=1, day=1, hour=0, minute=0, second=0):
        """获取某一时间
        datetime.datetime.today()
        """
        datetime_obj = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
        return datetime_obj

    def get_cur_month_first_weekday_month_range(self, year, month):
        """获取某年某月有多少天和第一天是周几"""
        week_day, month_range = calendar.monthrange(year, month)
        return week_day, month_range

    def get_datetime_from_timestamp(self, timestamp):
        """时间戳 --> datetime时间格式"""
        return datetime.datetime.fromtimestamp(timestamp)

    def datetime_to_timestamp(self, datetime_obj):
        """datetime时间格式 --> 时间元组格式(time.struct_time) --> 时间戳"""
        timestamp_obj = time.mktime(datetime_obj.timetuple())
        return timestamp_obj

    def date_str_to_datetime(self, date_str, str_format):
        """日期字符串 --> datetime时间格式
        '%a %b %d %H:%M:%S %z %Y'： 'Fri Jan 22 17:56:48 +0800 2021'
        '%Y-%m-%d %H:%M:%S': 2021-01-22 17:56:48
        在datetime中定义的周,月的英文缩写： datetime._DAYNAMES, datetime._MONTHNAMES
        """
        return datetime.datetime.strptime(date_str, str_format)

    def datetime_to_date_str(self, datetime_obj, str_format):
        """datetime时间格式 --> 日期字符串"""
        return datetime.datetime.strftime(datetime_obj, str_format)

    def datetime_timezone_transform(self, datetime_obj, zone: pytz.timezone):
        """zone = timezone('Asia/Shanghai') 东八区
        转换时区到指定时区对象的时间，并指明相对于0时区的时间是超过还是推迟约几个小时
        """
        return datetime_obj.astimezone(zone)

    def print_all_timezones(self):
        """获取所有时区
            GMT格林威治时间, 0时区时间
            UTC世界标准时间, 0时区时间
            UTC由GMT计算而来，比GMT更精确
            ISO是时间展示格式, 中国采用Asia/Shanghai的东八区时间
        """
        return pytz.all_timezones

    def add_time_zones_info(self, datetime_obj):
        """在时间对象中的天与时之间插入字母T"""
        return datetime_obj.isoformat()

    def get_calendar_month(self, year, month):
        """打印出某年某月的月历"""
        return calendar.month(year, month)


if __name__ == '__main__':
    uc = UserConfig()
    config = uc.read_config()
    uc.write(key={"asswd": str(1123)})
    uc.check_config(config)
