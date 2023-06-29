# YYH rgb to hex的转换函数
def rgb_to_hex(red, green, blue):
    """%02x:在C语言中表示以十六进制输出,2为指定的输出字段的宽度.如果位数小于2,则左端补0,右对齐
    >>> rgb_to_hex((122,211,131))
    """
    return '#%02x%02x%02x' % (red, green, blue)


def rgb_to_hex_calc(rgb):
    """转换为16进制的颜色色值
    >>> rgb_to_hex((122,211,131))
    '#7ad383'
    """
    color = '#'
    for num in rgb:
        color += str(hex(num))[-2:].replace('x', '0').upper()
    return color.lower()


def hex_to_rgb_builtins(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def get_color(color, rgb_func_call):
    color_type = type(color)
    if color_type in (tuple, list) and len(color) == 3:
        pass
    elif color_type is str:
        color = rgb_func_call(color)
    else:
        raise ValueError("Unsupported type %s in set_color()")

    color_rang = []
    for number in color:
        if number > 255:
            number = 255
        elif number < 0:
            number = 0
        else:
            number = number
        color_rang.append(int(number))
    return color_rang