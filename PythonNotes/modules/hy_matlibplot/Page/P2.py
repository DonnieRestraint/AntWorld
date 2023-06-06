import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.ticker import MultipleLocator


def set_bg(fig, ax, x_list, y_lim, labels):
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
    set_half_bg(fig, ax, x_list[0], median, x_list, y_lim, labels[0], 36, "red")
    set_half_bg(fig, ax, median, x_list[-1], x_list, y_lim, labels[1], 24, "green")


def set_half_bg(fig, ax, left, right, x_range, y_lim, text, fontsize, color):
    """设置半边背景，锚点左上角"""
    text_width, text_height = get_text_size(fig, ax, text, fontsize)
    axes_width, axes_height = get_axes_size(fig, ax)

    rect_width, rect_height = get_rect_size(fig, text_width, text_height, axes_width, axes_height, x_range, y_lim)
    # 添加区域与文本
    ax.add_patch(Rectangle((left, y_lim[0]), right - left, y_lim[1] - y_lim[0], fc=color, ec='g', lw=1, alpha=0.1))
    ax.add_patch(Rectangle((left, y_lim[1] - rect_height), rect_width, rect_height, fc=color, ec='g', lw=1, alpha=0.5))
    ax.text(left + rect_width / 2, y_lim[1] - rect_height / 2, text, fontsize=fontsize, color='black', horizontalalignment='center', verticalalignment='center', alpha=0.8)


def get_rect_size(fig, text_width, text_height, axes_width, axes_height, x_range, y_lim):
    """通过像素获取在坐标(x,y)刻度偏移量"""
    figure_bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    figure_width, figure_height = figure_bbox.width, figure_bbox.height
    rect_width = text_width + text_height
    rect_height = text_height + text_height
    point_x = (rect_width / axes_width) * (x_range[-1]-x_range[0])
    point_y = (rect_height / axes_height) * (y_lim[-1]-y_lim[0])
    return point_x, point_y


def get_figure_size(fig):
    """get px of figure"""
    bbox = fig.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    return bbox.width * fig.dpi, bbox.height * fig.dpi


def get_axes_size(fig, ax):
    """get px of axes(坐标系)"""
    bbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    width, height = bbox.width * fig.dpi, bbox.height * fig.dpi
    return width, height


def get_text_size(fig, axes, text, fontsize):
    """通过部件对get_window_extent的调用获取像素值， 这里是axes.text()"""
    t_obj = axes.text(0, 0, text, fontsize=fontsize, color="white", alpha=0)
    bbox = t_obj.get_window_extent(renderer=fig.canvas.get_renderer())
    return bbox.width, bbox.height


def demo2(figsize, labels):
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=figsize, gridspec_kw={'width_ratios': [12, 1]}, )  # 創建雙軸plot

    fig.set_facecolor('grey')
    ax0.set_facecolor("grey")
    # x = list(range(1, 11))
    # y = list(range(1, 11))
    # x_range = [0, 11]
    # y_range = [0, 10]
    x = [1]
    y = [1]
    x_range = [0, 2]
    y_range = [0, 2]
    # plt.rcParams['savefig.dpi'] = 100  # 图片像素
    # plt.rcParams['figure.dpi'] = 100  # 分辨率
    print(plt.rcParams['savefig.dpi'])
    print(plt.rcParams['figure.dpi'])
    # plt.xlim(x_range)
    ax0.set_xlim(x_range)
    ax0.set_ylim(y_range)
    # plt.xticks(x, ["a"])
    # plt.yticks(y, ["b"])
    ax0.xaxis.set_major_locator(MultipleLocator(1))
    ax0.yaxis.set_major_locator(MultipleLocator(1))
    ax0.plot(x, y, c="black")
    ax0.set_xlim(x_range)
    ax0.set_xlim(y_range)
    # plt.xlim(x_range)
    # plt.ylim(y_range)
    # 设置轴的颜色
    ax0.spines["top"].set_color("none")
    ax0.spines["bottom"].set_position(("data", 0))
    set_bg(fig, ax0, x, y_range, labels)

    plt.show()
    plt.savefig("img004.png")
    plt.clf()


if __name__ == '__main__':
    demo2((19.2, 10.8), ["Label", "LabelLabel"])