# Gradients in OpenCV to find the edges generally

import cv2
import numpy as np

img = cv2.imread('photos/waste/ney.png') #reads the image

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Laplacian
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow('laplacian',lap)

# Sobel
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1,0)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0,1)
combined_sobel = cv2.bitwise_or(sobelx, sobely)
# cv2.imshow('sobelx',sobelx)
# cv2.imshow('sobely',sobely)
cv2.imshow('sobel',combined_sobel)
canny = cv2.Canny(gray,150,175)
cv2.imshow('canny',canny)
cv2.waitKey(0)