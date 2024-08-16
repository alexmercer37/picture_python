
    
    
    # !/usr/bin/env python
# -*- coding: utf-8 -*-
# ============================================================
# @Date    : 2021/12/08 14:40:31
# @Author  : LiShan
# @Email   : lishan@st.xatu.edu.com
# @File    : extract.py
# @IDE     : PyCharm
# @Func    : Extract video image
# ============================================================
import os.path
import time
import cv2
 
video_path = "/home/dxy/Downloads/python/video.mp4"
save_path = video_path[:video_path.rfind('.')]
os.makedirs(save_path, exist_ok=True)
cap = cv2.VideoCapture(video_path)
fps = int(cap.get(cv2.CAP_PROP_FPS))
print('FPS:{:.2f}'.format(fps))
rate = cap.get(5)
frame_num = cap.get(7)
duration = frame_num/rate
print('video total time:{:.2f}s'.format(duration))
 
# width, height = 1920, 1080
# interval = int(fps) * 4
interval = 1
process_num = frame_num // interval
print('process frame:{:.0f}'.format(process_num))
 
cnt = 0
num = 0
 
t0 = time.time()
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cnt += 1
        if cnt % interval == 0:
            num += 1
            # frame = cv.resize(frame, (width, height))
            cv2.imwrite(save_path + "/%04d.jpeg" % num, frame)
            remain_frame = process_num - num
            t1 = time.time() - t0
            t0 = time.time()
            print("Processing %04d.jpg, remain frame: %d, remain time: %.2fs" % (num, remain_frame, remain_frame * t1))
    else:
        break
    if cv2.waitKey(1) & 0xff == 27:
        break
 
cap.release()
cv2.destroyAllWindows()
print("done")

