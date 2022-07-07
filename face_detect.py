# Code to detect a face using Haar Cascade

import cv2
img = cv2.imread('photos/waste/group.jpg') #reads the image
img = cv2.resize(img, (700,500))
cv2.imshow('ney', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray person',gray)

haar_cascade = cv2.CascadeClassifier('C:\\Coding\\ML Practice\\CV2 practise\\haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 7)
# When i put neighbours = 3...14 faces were found, but when i increased it to 7 it became 11 faces (all correct)


print(f'no. of faces = {len(faces_rect)}')
for (x,y,w,h) in faces_rect:
    cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0), 2)

cv2.imshow('detected faces',img)
cv2.waitKey(0)