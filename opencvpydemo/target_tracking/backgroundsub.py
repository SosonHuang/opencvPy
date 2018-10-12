import cv2
import numpy as np
from matplotlib import pyplot as plt

camera = cv2.VideoCapture(0)
mog = cv2.createBackgroundSubtractorMOG2()

while(1):
  ret, frame = camera.read()
  fgmask = mog.apply(frame)
  cv2.imshow('frame',fgmask)
  # if cv2.waitKey(300) & 0xff:
  #   break

camera.release()
cv2.destroyAllWindows()
