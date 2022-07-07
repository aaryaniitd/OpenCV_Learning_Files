# Code to draw on an Image

import cv2
# from cv2 import circle
import numpy as np


blank = np.zeros((500,500,3), dtype='uint8')

# cv2.imshow('blank',blank)
# img = cv2.imread('C:\\Coding\\ML Practice\\CV2 practise\\photos\\ney.png') #reads the image
# cv2.imshow('ney', img)

# Paint the image a certain colour
# blank[200:300,:] = 255,255,255
# cv2.imshow('mix', blank)

# Draw a Rectangle
cv2.rectangle(blank, (blank.shape[0]//2,blank.shape[1]//4), (0,0), (255,255,255), thickness = -1)
# Draw a circle
cv2.circle(blank, (250,250), blank.shape[0]//4, color = (0,0,255), thickness=-1)
#Draw a line
cv2.line(blank, (0,0), (500,500), (255,0,0), thickness= 3)

# Write Text
cv2.putText(blank, 'Hello', (100,450), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0))
cv2.imshow('CUSTOM',blank)

cv2.waitKey(0)