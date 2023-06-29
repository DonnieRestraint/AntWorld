import numpy as np
import cv2
# 1.获取视频对象
cap = cv2.VideoCapture('./videos_1.mp4')
# 2.判断是否读取成功
while(cap.isOpened()):
    # 3.获取每一帧图像
    ret, frame = cap.read()
    # 4. 获取成功显示图像
    if ret == True:
        cv2.imshow('frame',frame)
    # 5.每一帧间隔为25ms,
    # cv2.waitKey(25) & 0xFF，由cv2.waitKey捕捉到的键盘ascii值与0xFF位与，只留下最后8位，遵循了CC BY-SA 3.0 许可协议
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
# 6.释放视频对象
cap.release()
cv2.destroyAllWindows()