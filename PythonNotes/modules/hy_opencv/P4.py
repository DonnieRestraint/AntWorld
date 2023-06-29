import os
import cv2
import numpy as np
import time


def cover_img_to_avi(dir_path, img_type="jpg"):
    """
    ffmpeg
    参数/编码类型/文件后缀名，i420格式
    cv2.VideoWriter_fourcc('I', '4', '2', '0')	该参数是YUV编码类型	.avi √
    cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')	该参数是MPEG-4编码类型	.avi √
    cv2.VideoWriter_fourcc('F', 'L', 'V', '1')	该参数是Flash视频	.flv √
    cv2.VideoWriter_fourcc('m', 'p', '4', 'v')	该参数是Flash视频	.mp4 √

    """
    filelist = os.listdir(dir_path)
    # 视频每秒25帧
    fps = 16
    # 需要转为视频的图片的尺寸
    size = (640, 360)
    # 编码类型
    code_type = ('m', 'p', '4', 'v')
    # 文件后缀名
    mp4 = ".mp4"
    # 视频保存在当前目录下
    video_name = time.strftime("%Y_%m_%d_%H_%M_%S", time.gmtime())
    video = cv2.VideoWriter(video_name + mp4, cv2.VideoWriter_fourcc(*code_type), fps, size)

    for item in filelist:
        if item.endswith(img_type):
            # jpg和png都可以合成
            item = os.path.join(dir_path, item)
            img = cv2.imread(item)
            # 使用cv2.resize()适配定义的尺寸
            img = cv2.resize(img, size)
            video.write(img)

    video.release()
    cv2.destroyAllWindows()

    
cover_img_to_avi("test")

