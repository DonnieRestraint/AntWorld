import os
import cv2
from cv2 import VideoCapture
import shutil
import time


def extract_frames(video_path, dst_folder, frame_sample, index):
    """
    {:>03d}.jpg.format(int) 表示格式化为3位数字左侧补零
    """
    # 实例化视频对象
    video = cv2.VideoCapture(video_path)
    frame_count = 0

    # 循环遍历视频中的所有帧
    while True:
        # 逐帧读取
        _, frame = video.read()
        if frame is None:
            break
        # 按照设置的频率保存图片
        if frame_count % frame_sample == 0:
            # 设置保存文件名
            save_path = "{}/{:>03d}.jpg".format(dst_folder, index)
            # 保存图片
            cv2.imwrite(save_path, frame)
            index += 1  # 保存图片数＋1
        frame_count += 1  # 读取视频帧数＋1

    # 视频总帧数
    print(f'the number of frames: {frame_count}')
    # 打印出所提取图片的总数
    print("Totally save {:d} imgs".format(index - 1))
    # 计算FPS get() 或 总帧数 / 总时间
    (major_ver, minor_ver, subminor_ver) = cv2.__version__.split('.')  # Find OpenCV version
    # (major_ver, minor_ver, subminor_ver) = (4, 5, 4)
    if int(major_ver) < 3:
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)  # 获取当前版本opencv的FPS
        print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else:
        fps = video.get(cv2.CAP_PROP_FPS)  # 获取当前版本opencv的FPS
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))


if __name__ == '__main__':
    EXTRACT_FOLDER = 'test'  # 存放帧图片的位置
    try:
        shutil.rmtree(EXTRACT_FOLDER)
    except OSError:
        pass
    os.mkdir(EXTRACT_FOLDER)
    # 视频地址
    VIDEO_PATH = 'cover_v.mp4'
    # 帧均值抽样
    EXTRACT_FREQUENCY = 1
    # 抽取帧图片，并保存到指定路径
    extract_frames(VIDEO_PATH, EXTRACT_FOLDER, EXTRACT_FREQUENCY,1)
