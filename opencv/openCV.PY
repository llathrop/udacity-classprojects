#!/bin/python
from mystatslib import *
import math
import time
 
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg')
orig = img
gray = cv2.imread('messi5.jpg')
img1 = cv2.imread('m1.jpg')
img2 = cv2.imread('opencv-logo-white.png')


try:
    cap = cv2.VideoCapture(0)
except IOError as (errno, strerror):
    print "I/O error({0}): {1}".format(errno, strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise

try:
    _, frame = cap.read()
except IOError as (errno, strerror):
    print "I/O error({0}): {1}".format(errno, strerror)
except ValueError:  
    print "Could not convert data to an integer."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise    
print "cam image params:"
print frame.shape
print frame.size
print frame.dtype

    
# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
font = cv2.FONT_HERSHEY_SIMPLEX
frameNum =0

while(1):
    e1 = cv2.getTickCount()
    # Take each frame
    try:
        _, frame = cap.read()
    except IOError as (errno, strerror):
        print "I/O error({0}): {1}".format(errno, strerror)
    except ValueError:
        print "Could not convert data to an integer."
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
    frameNum+=1     
    height, width = frame.shape[:2]
    rows, cols = height, width
    
    #Convert to gray
    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    #use a histogram to equalize, using a CLAHE object
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    equalized = clahe.apply(gray)
    #equalized = cv2.equalizeHist(gray)    
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
#    res = cv2.resize(res,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

#rotate
#    M = cv2.getRotationMatrix2D((cols/2,rows/2),frameNum,1)
#offset
#    M = np.float32([[1,0,frameNum],[0,1,frameNum]])
#apply 
#    frame = cv2.warpAffine(frame,M,(cols,rows)) 

#smooth/blur, that kind of thing
    blur = cv2.bilateralFilter(equalized,9,75,75)
    median = cv2.medianBlur(blur,11)
    #laplacian = cv2.Laplacian(blur,cv2.CV_64F)
    #sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)
    #sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)
#threshold the image
    #thresh1 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.ADAPTIVE_THRESH_MEAN_C,11,2)
    thresh2 = cv2.adaptiveThreshold(median,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,15,2)
    
    #ret3,thresh3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #denoise?
    
# Edges
    kernel = np.array([1,0,-1])    
    edges = cv2.filter2D(equalized,-1,kernel)
    edgesblurred = cv2.filter2D(thresh2,-1,kernel)
    edgesCanny= cv2.Canny(equalized,100,200)    
   
# contours
    input=thresh2 
    out, contours, hierarchy = cv2.findContours(input,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    out, contours, hierarchy = cv2.findContours(input, 1, 2)
    
    #contoursFrame = cv2.drawContours(frame, contours, -1, (0,255,0), 3)
    print frameNum,len(contours)
    cnt = contours[frameNum%(len(contours))]
    moments = cv2.moments(cnt)
    M=moments
    #cx = int(M['m10']/M['m00'])
    #cy = int(M['m01']/M['m00'])
    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt,True)
    epsilon = 0.1*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    hull = cv2.convexHull(cnt)
    
    #use something as a mask on the camera
    res = cv2.bitwise_and(frame,frame, mask= out)
    #draw around the contour
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    contoursFrame = cv2.drawContours(res,[box],0,(0,0,255),2)
    #contoursFrame = cv2.drawContours(frame,approx,0,(0,0,255),2)
    
   
    #sidebyside display--use cv2.cvtColor(<IMAGE>, cv2.COLOR_GRAY2BGR) to convert to color if needed
    #disp =  np.hstack((gray,equalized))
    disp =  np.hstack((contoursFrame,cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)))
    # timer code
    e2 = cv2.getTickCount()
    timer = (e2 - e1)/ cv2.getTickFrequency()
    #text in update
    dispText= "frame:"+str(frameNum) + " time:"+str(timer)
    cv2.putText(disp,dispText,(20,25), font, 1,(255,255,255),2,cv2.LINE_AA)
    #display the above
    cv2.imshow('OpenCV',disp)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

print "Frame num: ", frameNum

#EOF

