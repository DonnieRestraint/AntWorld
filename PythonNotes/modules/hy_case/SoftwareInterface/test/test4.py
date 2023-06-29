"""
从第三方模块内置的模型提取视频中的数据
"""
# pip install opencv-python
import cv2
# pip install matplotlib
import matplotlib.pyplot as plt

data = cv2.VideoCapture(r'./videos_1.mp4')
j = 1
face_cascade = cv2.CascadeClassifier(
    'D:\SOFTSPACE\Anaconda3\envs\gic\Lib\site-packages\cv2\data/haarcascade_frontalface_default.xml')  # 要提取opencv中一个xml文件


def search_face(img):
    global j
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转为灰度图片，这样才能提取人脸
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # 找人脸
    if faces == ():  # 如果某一帧找不到人脸，则返回0
        return 0
    else:
        for (x, y, w, h) in faces:
            try:
                img = img[y - 20:y + h + 20:, x - 20:x + w + 20:, :]  # 人脸的宽度长度
                cv2.imwrite(r'.\imgs\%d.jpg' % j, img)  # 写入本地
                print("第%d张人脸图片" % j)
                j = j + 1
            except:
                pass


ret, frame = data.read()  # 读取video
i = 0
# 如果ret不为空，即能在某一帧中提取人脸图片
while ret:
    ret, frame = data.read()
    if ret == True:
        i = i + 1
        if i % 20 == 0:
            search_face(frame)
        # 展示图片
        # cv2.imshow('frame', frame)
    # if cv2.waitKey(5) & 0xFF == ord('q'):
    #     break
data.release()  # 释放内存
cv2.destroyAllWindows()
