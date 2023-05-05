# 中文包过生僻字
ChineseRegex = r"/^((?![\u3000-\u303F])[\u2E80-\uFE4F]|\·)*(?![\u3000-\u303F])[\u2E80-\uFE4F](\·)*$/"
# 数字
r2 = r"^[+-]?\d+(.\d+)?$"
# 邮箱
r3 = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
# 手机号
# 前三位是网络识别号， 中间4位是地区编码， 后4位是用户号码
r4 = r'^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$'
# 身份证
# 第一位1-9/后面5位0-9/年份1,2开头，后面三位0-9/月份/日期/3位数字0-9/最后一位0-9xX
r5 = r'^([1-9]\d{5}([12]\d{3})(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])\d{3}[0-9xX])$'


if __name__ == '__main__':
    import re
