import cv2
import numpy as np
import math

capture = cv2.VideoCapture(2)
while True:
    ref, img = capture.read()
    blue_lower = np.array([125, 43, 46])
    blue_upper = np.array([155, 255, 255])
    # blue_lower = np.array([0, 43, 46])
    # blue_upper = np.array([10, 255, 255])
    # blue_lower = np.array([100, 43, 46])
    # blue_upper = np.array([124, 255, 255])
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img_HSV, lowerb= blue_lower, upperb= blue_upper)
    img_ball = cv2.bitwise_and(img, img, mask= mask)
    img_ball = cv2.cvtColor(img_ball, cv2.COLOR_BGR2GRAY)
    cv2.imshow('img_ball', img_ball)
    __, img_bin = cv2.threshold(img_ball, 10, 255, cv2.THRESH_BINARY)
    contours, __ = cv2.findContours(img_bin,  cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    area = []
    for i in range(len(contours)):
        mianji = cv2.contourArea(contours[i])
        area.append(mianji)
    max_area_num = np.argmax(area)
    cnt = contours[max_area_num]
    print(cnt)
    x, y, w, h = cv2.boundingRect(cnt)
    img_juxing = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2)
    x1 = int(x+w/2)
    y1 = int(y+h/2)
    Center_point_x = int(img.shape[0]/2)
    Center_point_y = int(img.shape[1]/2)
    img_juxing = cv2.line(img_juxing, (x1,y1), (Center_point_x,Center_point_y),(0,0,255),2)
    s_l = math.pow(abs(Center_point_x - x1), 2)
    s_w = math.pow(abs(Center_point_y - y1), 2)
    s = int(math.sqrt(s_l + s_w))
    print(s)
    img_juxing = cv2.putText(img, str(s), (x,y), cv2.FONT_HERSHEY_COMPLEX, 1,(255,0,0), 2)
    cv2.imshow('img_wenben', img_juxing)
    cv2.waitKey(1)
    if cv2.waitKey(1)==27:
        cv.destroyAllWindows()
        break

# import cv2 as cv
 
# # 0是代表摄像头编号，只有一个的话默认为0
# capture = cv.VideoCapture(0)
# while True:
#     # 调用摄像机
#     ref, frame = capture.read()
#     # 输出图像,第一个为窗口名字
#     cv.imshow('PC Camera', frame)
#     # 等待5秒显示图像，若过程中按“Esc”（key=27）退出
#     c = cv.waitKey(5) & 0xff
#     if c == 27:
#         # 释放所有窗口
#         cv.destroyAllWindows()
#         break

