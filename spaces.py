# Code describing how to translate between colour spaces

import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('photos/waste/ney.png') #reads the image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray',gray)

# BGR to HSV (heu saturation value)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow('hsv',hsv)

# BGR to l*a*b
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
# cv2.imshow('lab',lab) 

# BGR to RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imshow('rgb',rgb)
# plt.imshow(rgb)
# plt.show()

# HSV to BGR
hsv_bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow('hsv_bgr',hsv_bgr)

# LAB to BGR
lab_bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
cv2.imshow('lab_bgr',lab_bgr)

cv2.waitKey(0)