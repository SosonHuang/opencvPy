#-*- coding=utf-8 -*-
import cv2
import numpy as np
import sys

img = cv2.imread('images/chess_board.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

#检测焦点特征函数
dst = cv2.cornerHarris(gray, 9, 23, 0.04)
img[dst>0.01 * dst.max()] = [0, 0, 255] 
while (True):
  cv2.imshow('corners', img)
  if cv2.waitKey(1000 / 12) & 0xff == ord("q"):
    break
cv2.destroyAllWindows()
