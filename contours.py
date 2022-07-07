# Contours are similar to Edges but a much more mathematical topic, they are used to find lines which have a 
# constant inclination across

import cv2
from cv2 import Canny
import numpy as np
img = cv2.imread('photos/waste/ney.png') #reads the image

blank = np.zeros(img.shape,dtype='uint8')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray',gray)
blur = cv2.blur(gray, (5,5), cv2.BORDER_DEFAULT)
# cv2.imshow('blur',blur)
canny = cv2.Canny(img, 125,175)
# cv2.imshow('canny edges', canny)

ret, thresh = cv2.threshold(gray, 125,255, cv2.THRESH_BINARY)
cv2.imshow('thresh',thresh)
contours, hierarchies = cv2.findContours(thresh, mode= cv2.RETR_LIST, method = cv2.CHAIN_APPROX_SIMPLE)
# contours is a python list of coordinates of all the contours
# hierarchies is a method used by open cv to see what is inside what
print(len(contours))

cv2.drawContours(blank, contours, -1, (0,0,255),1)
cv2.imshow('contours',blank)
cv2.waitKey(0)