# The remaining part of faces_train.py.....Deploying the model and testing it

import numpy as np
import cv2
people = ['Cristiano Ronaldo', 'Lionel Messi', 'Neymar Junior', 'Robert Lewandowski', 'Dani Alves','Luka Modric','Kevin De Bruyne','Karim Benzema','Sergio Ramos', 'Luis Suarez']

haar_cascade = cv2.CascadeClassifier('haar_face.xml')
features = np.load('features.npy',allow_pickle=True)
labels = np.load('labels.npy', allow_pickle=True)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')


img = cv2.imread(r'photos/waste/n.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('person',gray)

# Detect faces in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1,7)
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+h]
    label,confidence = face_recognizer.predict(faces_roi)
    print(f'label={people[label]} with a confidence of {confidence}')
    cv2.putText(img, str(people[label]), (20,20),cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),thickness=2)

cv2.imshow('Detected Face', img)  

cv2.waitKey(0)
