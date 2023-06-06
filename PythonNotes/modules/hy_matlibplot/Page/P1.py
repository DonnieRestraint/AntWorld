import os
import sys

from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    path = os.path.join(base_path, relative_path)
    return path


def get_file(path):
    print(resource_path(path))
    if os.path.exists(path):
        return path
    else:
        return resource_path(path)


def get_font(ttf_path, size):
    try:
        ttf_path = get_file(ttf_path)
        font = ImageFont.truetype(ttf_path, size=size)
        return font
    except Exception as err:
        print("Not Found font %s" % ttf_path)
        return ImageFont.load_default()


def get_png(figsize, labels):
    width, height = int(figsize[0] * 100), int(figsize[1] * 100)
    label_left, label_right = labels
    origin_point = (0, 0)
    midpoint = (width / 2, 0)
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    draw = ImageDraw.Draw(img)
    font = get_font('fonts/Montserrat.ttf', int(height/20))
    draw.rectangle((origin_point, (width / 2, height)), fill=(255, 0, 0, 20), outline=(255, 0, 0, 20))
    draw.rectangle((midpoint, (width, height)), fill=(0, 255, 0, 20), outline=(0, 255, 0, 20))

    label_left_rect = draw.textsize(label_left, font)
    print(label_left_rect)
    rect_width, rect_height = int(label_left_rect[0] + label_left_rect[1]), int(label_left_rect[1] * 2)

    shape_left = [origin_point, (rect_width, rect_height)]
    draw.rectangle(shape_left, fill=(255, 0, 0, 50), outline=(255, 0, 0, 60))
    draw.text(xy=(rect_width / 2 - label_left_rect[0] / 2, rect_height / 2 - label_left_rect[1] / 2 - 3), text=label_left, fill='black', font=font)

    label_right_rect = draw.textsize(label_right, font)
    print(label_right_rect)
    rect_width, rect_height = int(label_right_rect[0] + label_right_rect[1]), int(label_right_rect[1] * 2)

    shape_right = [midpoint, (width / 2 + rect_width, rect_height)]
    draw.rectangle(shape_right, fill=(0, 255, 0, 50), outline=(0, 255, 0, 60))
    draw.text(xy=(width / 2 + rect_width / 2 - label_right_rect[0] / 2, rect_height / 2 - label_right_rect[1] / 2 - 3), text=label_right, fill='black', font=font, align="center")

    # img.save("img001.png")
    # img.show()

    io_bytes = BytesIO()
    img.save(io_bytes, format="PNG")
    return io_bytes


def demo(img_io):
    figsize = (19.2, 10.8)
    f, (ax0, ax1) = plt.subplots(1, 2, figsize=figsize, gridspec_kw={'width_ratios': [12, 1]})  # 創建雙軸plot

    # img = plt.imread("../images/DesenseOtaReport.png")
    img = plt.imread(img_io, format="PNG")
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    x_range = [0, 24]
    y_range = [0, 12]
    plt.xlim(x_range)
    plt.ylim(y_range)
    ax0.imshow(img, extent=[*x_range, *y_range])
    ax0.plot(x, y, c="black")

    # plt.show()
    plt.savefig("img003.png")


def paint_plt(ax, x_list, y_lim, labels, step):
    from matplotlib.patches import Rectangle
    import numpy as np
    if len(x_list) == 1:
        x_step = 1
        median = x_list[0]
    elif len(x_list) > 1:
        x_step = x_list[1] - x_list[0]
        median = np.median(x_list)
    else:
        return

    x_list.insert(0, x_list[0] - x_step)
    x_list.append(x_list[-1] + x_step)

    if len(x_list) % 2 == 0:
        x_list.insert(int(len(x_list)/2), median)

    width_rect, height_rect = (x_list[-1]-x_list[0])/10, (y_lim[-1]-y_lim[0])/10

    # 添加区域与文本
    ax.add_patch(Rectangle((x_list[0], y_lim[0]), median-x_list[0], y_lim[-1]-y_lim[0], fc='red', ec='g', lw=1, alpha=0.1))
    ax.add_patch(Rectangle((x_list[0], y_lim[1] - height_rect), width_rect, height_rect, fc='red', ec='g', lw=1, alpha=0.2))
    ax.text(x_list[0] + width_rect/2, y_lim[1] - height_rect/2, labels[0], fontsize=12, color='black', horizontalalignment='center', verticalalignment='center')

    ax.add_patch(Rectangle((median, y_lim[0]), x_list[-1]-median, y_lim[-1]-y_lim[0], fc='green', ec='g', lw=1, alpha=0.1))
    ax.add_patch(Rectangle((median, y_lim[1] - height_rect), width_rect, height_rect, fc='green', ec='g', lw=1, alpha=0.2))
    ax.text(median + width_rect/2, y_lim[1] - height_rect/2, labels[1], fontsize=12, color='black', horizontalalignment='center', verticalalignment='center')
    # bbox = dict(facecolor='green', alpha=0.3, edgecolor='none', boxstyle="square, pad=0.3")


if __name__ == '__main__':
    io_img = get_png((19.2, 10.8), ["Label", "LabelLabel"])
    demo(io_img)
    import time
    time.sleep(20)