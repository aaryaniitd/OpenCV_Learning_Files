# Making image transformation like rotating, flipping, resizing, cropping

# from turtle import down, left, right, up
import cv2
import numpy as np

img = cv2.imread('photos/waste/ney.png') #reads the image

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up
# +x --> right
# +y --> down    

translated = translate(img, -100,-199)
# cv2.imshow('translated', translated)

#  Rotation
def rotate( img, angle, rotPoint=None):
    (height, width) = img.shape[0], img.shape[1]
    if rotPoint is None:
        rotPoint= (width//2, height//2)
    rotMat=cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv2.warpAffine(img, rotMat, dimensions)
rotated = rotate(img, 45)
# temp = [rotated]
# for i in range(1,10):
#     temp.append(rotate(temp[i-1],45))
# cv2.imshow('Rotated', temp[-1])

# Resize
resized = cv2.resize(img, (400,400), interpolation=cv2.INTER_AREA)
# cv2.imshow('resized',resized)

# flipping
flip = cv2.flip(img, 1) # 1 means horizontal flip and 0 means vertical flip
# cv2.imshow('flip', flip)

# cropping
cropped = img[200:, 300:]
cv2.imshow('cropped', cropped)
cv2.waitKey(0)