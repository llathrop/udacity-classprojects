#!/bin/python
from mystatslib import *
import math
 
import cv2
import numpy as np

cv2.namedWindow('image1', cv2.WINDOW_NORMAL)
cv2.namedWindow('image2', cv2.WINDOW_NORMAL)


img = cv2.imread('messi5.jpg')
print img.shape
print img.size
print img.dtype

cv2.imshow('image1',img)

px = img.item(10,10,2)
print px

for i in range(10, 100):
    img.itemset((i,i,2),200)

px = img.item(10,10,2)
print px

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

cv2.imshow('image2',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#EOF

