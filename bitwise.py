# This file carries the code for bitwise operations in OpenCV


import cv2
import numpy as np

img = cv2.imread('photos/waste/ney.png') #reads the image
 
blank = np.zeros((400,400), dtype='uint8')
rectangle = cv2.rectangle(blank.copy(), (30,30),(370,370),255,-1)
circle = cv2.circle(blank.copy(), (200,200),200,255,-1)
# cv2.imshow('rectangle', rectangle)
# cv2.imshow('circle',circle)

# Bitwise AND --> intersection
bitwise_and = cv2.bitwise_and(rectangle, circle)
cv2.imshow('bitwise AND', bitwise_and)

# Bitwise OR --> non-intersecting and intersecting
bitwise_or = cv2.bitwise_or(rectangle,circle)
cv2.imshow('bitwise_or',bitwise_or)

# Bitwise XOR --> non-intersecting
bitwise_xor = cv2.bitwise_xor(rectangle,circle)
cv2.imshow('bitwise_xor',bitwise_xor)
cv2.waitKey(0)