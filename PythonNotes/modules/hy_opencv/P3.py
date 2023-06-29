import cv2
import os
import numpy as np
"""
使用了模板变透明，并未真正处理图片
"""


def get_none_img(dir_path, img):
    """
    将绿幕图片抠成透明背景图片
    get_none_img(".", "green_img.png")
    """
    # 读取并转换图片格式
    file_name, ext = os.path.splitext(img)
    opencv = cv2.imread(os.path.join(dir_path, img))
    hsv = cv2.cvtColor(opencv, cv2.COLOR_RGB2HSV)

    # 指定绿色范围,60表示绿色，我取的范围是-+10
    minGreen = np.array([30, 70, 70])
    maxGreen = np.array([80, 255, 255])

    # 确定绿色范围
    mask = cv2.inRange(hsv, minGreen, maxGreen)

    # 确定非绿色范围
    mask_not = cv2.bitwise_not(mask)

    # 通过掩码控制的按位与运算锁定绿色区域
    green = cv2.bitwise_and(opencv, opencv, mask=mask)

    # 通过掩码控制的按位与运算锁定非绿色区域
    green_not = cv2.bitwise_and(opencv, opencv, mask=mask_not)

    # 拆分为3通道
    b, g, r = cv2.split(green_not)

    # 合成四通道
    bgra = cv2.merge([b, g, r, mask_not])

    # 保存带有透明通道的png图片,有了这种素材之后，就可以给这张图片替换任意背景了
    cv2.imwrite("none_{}.png".format(file_name), bgra)


def coverToTransparent(dir_path, file_type):
    """
    [200, 200, 200]为单一颜色分界线，滤色
    coverToTransparent(os.path.abspath("test"))
    """
    for file_name in os.listdir(dir_path):
        if file_name.endswith(file_type):
            continue
        path = os.path.join(dir_path, file_name)
        src = cv2.imread(path)
        # 如果要去掉水印，应当在此处理

        # Point 1: 生成与白色部分对应的mask图像
        mask = np.all(src[:, :, :] > [200, 200, 200], axis=-1)
        # Point 2: 将图片从三通道转为四通道
        dst = cv2.cvtColor(src, cv2.COLOR_BGR2BGRA)
        # Point3:  以mask图像为基础，使白色部分透明化
        dst[mask, 3] = 0
        # 保存图片
        cv2.imwrite("{}.png".format(os.path.splitext(path)[0]), dst)


def coverToWriteBackground(dir_path, file_type):
    """只是去掉背景"""
    for file_name in os.listdir(dir_path):
        if file_name.endswith(file_type):
            continue
        path = os.path.join(dir_path, file_name)

        # 不读取透明通道
        # dst = cv2.imread(path)

        # 转换4通道为3通道
        # src = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        # dst = cv2.cvtColor(src, cv2.COLOR_BGRA2BGR)
        # 降低透明度
        src = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        src[:, :, 3] = 200
        dst = src
        # 保存图片
        cv2.imwrite("{}.png".format(os.path.splitext(path)[0]), dst)


coverToTransparent(os.path.abspath("test"), "png")
# coverToWriteBackground(os.path.abspath("tiger"), "jpg")
# get_none_img(os.path.abspath("."), "green_img.png")
