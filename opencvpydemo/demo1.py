#-*- coding=utf-8 -*-

import numpy as np
import cv2
import os
#-*- coding=utf-8 -*-

import numpy as np
import cv2
import os

# img = np.zeros((3,3),dtype=np.uint8)
# print img
#
#
#
#
# #利用cv2.cvtColor函数将该图像转换成BGR格式
# img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
# print img
#
# #通过shape属性来查看图像的结构
# print img.shape
#
#
# #将加载的jpg文件作为灰度图像
# grayImage = cv2.imread('girl.jpeg',cv2.IMREAD_GRAYSCALE)
# cv2.imwrite('girlGray.jpeg',grayImage)
#
#
# #图像与原始字节之间的转换
# byteArray = bytearray(img)
# print bytearray


# #将含有随机字节的bytearray转换为灰度图像和BGR图像
# randomByteArray = bytearray(os.urandom(120000))
# flatNumpyArray = np.array(randomByteArray)
# #灰度图片
# grayImage1 = flatNumpyArray.reshape(300,400)
# cv2.imwrite('RandomGray.png',grayImage1)
#
# #带通道的图片
# bgrImage = flatNumpyArray.reshape(100,400,3)
# cv2.imwrite('RandomColor.png',bgrImage)


#使用numpy.array访问图像的数据
# img = cv2.imread('girl.jpeg')
# # 让坐标10，10的位置颜色设置为黑色
# img[10,10]=[0,0,0]
# img[11,11]=[0,0,0]
# img[12,12]=[0,0,0]
# cv2.imshow("img",img)
# cv2.waitKey(0)


#将指定通道（B，G，R）的所有值设置为0
# img = cv2.imread('girl.jpeg')
# img[:,:,1]=0
# cv2.imshow("img",img)
# cv2.waitKey(0)


#Numpy访问感兴趣区域（ROI）
# img = cv2.imread('girl.jpeg')
# #定义感兴趣的大小
# my_roi = img[0:100,0:100]
# #把感兴趣的mask，放入到指定的坐标位置
# img[300:400,300:400] = my_roi
# cv2.imshow("img",img)
# cv2.waitKey(0)



# img = cv2.imread('girl.jpeg')
# print img.shape  #返回宽，高，通道数，如果图片是单色或者灰度，将不包括通道值
# print img.size   #图像像素的大小
# print img.dtype  #图像的数据类型


#视频文件的读写/VideoCapture和VideoWriter
# videocapture = cv2.VideoCapture('WeChatSight1.avi')
# fps = videocapture.get(cv2.CAP_PROP_FPS)
# size = (int(videocapture.get(cv2.CAP_PROP_FRAME_WIDTH)),int(videocapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# videowriter = cv2.VideoWriter('myoutput.avi',cv2.VideoWriter_fourcc('I','4','2','0'),fps,size)
# sucess,frame = videocapture.read()
# while sucess:
#     videowriter.write(frame)
#     sucess,frame = videocapture.read()


#捕获摄像头的帧
# cameraCapture = cv2.VideoCapture(0)
# fps = 30
# size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# videowriter = cv2.VideoWriter('myoutput.avi',cv2.VideoWriter_fourcc('I','4','2','0'),fps,size)
# success,frame = cameraCapture.read()
# numFramesRemaining = 10 * fps - 1
# while success and numFramesRemaining > 0:
#     videowriter.write(frame)
#     sucess,frame = cameraCapture.read()
# cameraCapture.release()



#在窗口显示摄像头帧
# clicked = False
# def onMouse(event,x,y,flags,param):
#     global  clicked
#     if event == cv2.EVENT_LBUTTONUP:
#         clicked = True
# cameraCapture = cv2.VideoCapture(0)
# cv2.namedWindow('OpenCV')
# cv2.setMouseCallback('OpenCV',onMouse)
# success,frame = cameraCapture.read()
# while success and cv2.waitKey(1) == -1 and not clicked:
#     cv2.imshow('OpenCV',frame)
#     sucess,frame = cameraCapture.read()
# cv2.destroyWindow('OpenCV')
# cameraCapture.release()

# 边缘检测Canny函数
# 读取图片
# img = cv2.imread("girl.jpeg", 0)
# # 用canny函数处理过的图片，写入图片到到当前目录
# cv2.imwrite("canny.jpg", cv2.Canny(img, 200, 300))
# # 读取显示刚刚保存的canny图片
# cv2.imshow("canny", cv2.imread("canny.jpg"))
# cv2.waitKey()
# cv2.destroyAllWindows()



# 轮廓检测
# 创建200*200的黑色空白图像
img = np.zeros((200, 200), dtype=np.uint8)
# 在图片的中央放置一个白色方块
img[50:150, 50:150] = 255
# 对图片进行二值化操作
ret, thresh = cv2.threshold(img, 127, 255, 0)
# findContours 三个返回值，修改后的图片，图像的轮廓，它们的层次
#RETR_TREE 会得到图像中轮廓的整体结构
#RETR_EXTERNAL 得到最外面的轮廓
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
img = cv2.drawContours(color, contours, -1, (0,255,0), 2)
cv2.imshow("contours", color)
cv2.waitKey()
cv2.destroyAllWindows()