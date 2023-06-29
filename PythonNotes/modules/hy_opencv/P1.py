"""
HSV颜色模式偏向用户层模型
RGB颜色模式偏向硬件层模型

HSV:模型定义的范围；    opencv下的范围
    色调:0-360         0-180
    饱和度:0-1         0-255
    明度：0-1          0-255

    Hue, Saturation, Value.
    色调（H）： 红色为0°，绿色为120°，蓝色为240°， 它们的补色是：黄色为60°，青色为180°，紫色为300°
    饱和度（S）：表示色彩的鲜艳程度。 靠近0色彩越淡，靠近1色彩越纯。靠近0时，H无意义。
    亮度（V）：表示色彩明亮的程度。靠近0越暗，靠近1色彩越亮。靠近0时，H,S都无意义。

关于opencv在pycharm中没有代码提示的解决办法：
    已经安装上opencv的，可以通过pip install opencv-python 查看安装路径，如： Anaconda3/Lib/site-packages/cv2，
    windows中在cv2文件夹里找到cv2.pyd文件（ubuntu中是cv2文件夹中的.so文件）， 复制到上级目录（site-packages）等待pycharm解析完成
"""
import cv2
# imageSource = ""
# cv2.imread(imageSource)


def play(video_path):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow('frame', frame)
        # 5.每一帧间隔为25ms,
        # cv2.waitKey(25) & 0xFF，由cv2.waitKey捕捉到的键盘ascii值与0xFF位与，只留下最后8位，遵循了CC BY-SA 3.0 许可协议
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


play("cover_v.mp4")