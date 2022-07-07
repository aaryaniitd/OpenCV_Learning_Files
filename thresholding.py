# Any pixel having intensity above the threshold value will be considered to be existing, others will be discarded

import cv2 
import numpy as np
img = cv2.imread('photos/waste/ney.png') #reads the image
# cv2.imshow('ney',img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
# Simple Thresholding
threshold,thresh = cv2.threshold(gray, 100, maxval = 255, type=cv2.THRESH_BINARY )
cv2.imshow('simple thresholded',thresh)

threshold,thresh_inv = cv2.threshold(gray, 100, maxval = 255, type=cv2.THRESH_BINARY_INV )
cv2.imshow('simple thresholded inverse',thresh_inv)

# Adptive Threshold
adaptive_thresh = cv2.adaptiveThreshold(gray, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=11, C=3)

cv2.imshow('adaptive thresh',adaptive_thresh)
cv2.waitKey(0)