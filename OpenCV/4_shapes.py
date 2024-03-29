import cv2
import numpy as np
from numpy.lib.type_check import imag

img = np.zeros((512, 512, 3), np.uint8)
# print(img)
# print(img.shape)

# img[100:300,200:400]=255,0,0 #color the whole image if[:](h,w)

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 255), 3)
cv2.rectangle(img, (0, 0), (250, 350), (7, 255, 0), 2)
# cv2.rectangle(img,(0,0),(250,350),(7,255,0),cv2.FILLED)#fill rectangle

cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)

cv2.putText(img, "OPENCV", (300, 200),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 150, 0), 3)

cv2.imshow("Screen", img)

cv2.waitKey(0)
