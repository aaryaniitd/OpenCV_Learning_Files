# Split an image into constituent colour schemes and merging them back again

import cv2
import numpy as np

img = cv2.imread('photos/waste/ney.png') #reads the image
# cv2.imshow('ney',img)

blank = np.zeros(img.shape[:2],dtype = 'uint8')
b,g,r= cv2.split(img)

blue = cv2.merge([b,blank,blank])
green = cv2.merge([blank,g,blank])
red = cv2.merge([blank,blank,r])

cv2.imshow('blue',blue)
cv2.imshow('green',green)
cv2.imshow('red',red)
# print(img.shape)
# print(b.shape)
merged = cv2.merge([b,g,r])
cv2.imshow('merged',merged)

cv2.waitKey(0)