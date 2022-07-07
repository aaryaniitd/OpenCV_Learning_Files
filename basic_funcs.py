# This file holds code for basic functions on OpenCV - grayscaling, blurring, edge cascading, dilating, eroding
# resizing and cropping

import cv2

img = cv2.imread('photos/waste/ney.png') #reads the image
cv2.imshow('ney',img)


# converting to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)


# Blur
blur = cv2.GaussianBlur(img, (7,7), cv2.BORDER_DEFAULT)
# cv2.imshow('blur',blur)

# Edge Cascade
canny = cv2.Canny(img, 175, 175)
cv2.imshow('canny',canny)

# Dilating the image
dilated = cv2.dilate(canny, kernel = (7,7), iterations=3)
# cv2.imshow('dilated', dilated)

# Eroding
eroded = cv2.erode(dilated, (3,3), iterations=3)
# cv2.imshow('eroded', eroded)

# Resize
resized= cv2.resize(img, (500,500), interpolation=cv2.INTER_CUBIC)
# cv2.imshow('resized', resized)

# Cropping
cropped = img[250:350, 250:400]
cv2.imshow('cropped', cropped)

cv2.waitKey(0)