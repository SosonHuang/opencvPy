#-*- coding=utf-8 -*-
import cv2
import numpy as np
import io
from scipy import ndimage


kernel_3x3 = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])

kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                       [-1,  1,  2,  1, -1],
                       [-1,  2,  4,  2, -1],
                       [-1,  1,  2,  1, -1],
                       [-1, -1, -1, -1, -1]])

#转换为灰度图
img = cv2.imread("girl.jpeg",0)

#卷积
k3 = ndimage.convolve(img, kernel_3x3)
k5 = ndimage.convolve(img, kernel_5x5)


blurred = cv2.GaussianBlur(img, (17,17), 0)
g_hpf = img - blurred
cv2.namedWindow('3x3', 0)
cv2.imshow("3x3", k3)
cv2.namedWindow('5x5', 0)
cv2.imshow("5x5", k5)
cv2.namedWindow('g_hpf', 0)
cv2.imshow("g_hpf", g_hpf)
cv2.waitKey(0)
cv2.destroyAllWindows()