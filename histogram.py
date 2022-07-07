# plotting histograms in OpenCV for the colour intensities 

import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('photos/waste/ney.png') #reads the image
cv2.imshow('ney',img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Grayscale histogram
# gray_hist = cv2.calcHist([gray], [0], None, [256], [0,256])
# plt.figure()
# plt.title('grayscale histogram')
# plt.xlabel('bins')
# plt.ylabel('no. of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Colour Histogram

plt.figure()
plt.title('grayscale histogram')
plt.xlabel('bins')
plt.ylabel('no. of pixels')
colors = ['b','g','r']
for i,col in enumerate(colors):
    hist = cv2.calcHist([img],[i],None, [256],[0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()    

cv2.waitKey(0)