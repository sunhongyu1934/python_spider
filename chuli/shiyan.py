import cv2
import numpy as np

im=cv2.imread('C:/Users/Administrator/Desktop/bb.tif')

th=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
lower_blue = np.array([0,0,46])
upper_blue = np.array([180,43,220])
mask = cv2.inRange(th, lower_blue, upper_blue)

res = cv2.bitwise_and(im,im, mask= mask)

cv2.imshow('frame',im)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()

cv2.imwrite('C:/Users/Administrator/Desktop/206400.png',res)