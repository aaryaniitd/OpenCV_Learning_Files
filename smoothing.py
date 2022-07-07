# Code on various methods of Smoothening/Blurring

import cv2
import numpy as np

img = cv2.imread('photos/waste/ney.png') #reads the image
cv2.imshow('scenery',img)

# We blur by using the kernel method which computes a kernel and the final value is the value of the centre cell i.e., averaging method
# Averaging
average = cv2.blur(img, (3,3))
# cv2.imshow('average blur',average)

# Gaussian Blur - This also uses a kernel but this assigs weights to kernels and then sums over with the weights
gauss = cv2.GaussianBlur(img, (3,3), 0)
# cv2.imshow('gaussian blur',gauss)

# Median Blur - uses kernel but finds the median - good to reduce noise
median = cv2.medianBlur(img, 3)
# cv2.imshow('median blur', median)

# Bilateral Blurring - this retains the edges in the images
bilateral = cv2.bilateralFilter(img, 15, 35, 30)
cv2.imshow('bilateral blur',bilateral)

cv2.waitKey(0)