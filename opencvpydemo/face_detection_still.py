#-*- coding=utf-8 -*-
import cv2


#静态图片中的人脸检测
filename = 'images/girlgroup.jpeg'

def detect(filename):
  face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
  eye_cascade = cv2.CascadeClassifier('./cascades/haarcascade_eye.xml')
  img = cv2.imread(filename)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  #进行实际的人脸检测
  #传递参数是scaleFactor和minNeighbors，他们分别表示人脸检测过程中每次迭代时图像的压缩率以及每个人脸矩形保留近邻数目的最小值
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)

  #检测操作的返回值为人脸矩形数组，rectangle允许通过坐标来绘制矩形（x和y表示左上角的坐标，w和h表示人脸矩形的宽度和高度）
  for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
  
  cv2.namedWindow('Vikings Detected!!')
  cv2.imshow('Vikings Detected!!', img)
  cv2.imwrite('./vikings.jpg', img)
  cv2.waitKey(0)

if __name__ == "__main__":
     detect(filename)
