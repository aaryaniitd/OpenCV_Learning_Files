# Creating a model for face detection

import cv2
import numpy as np
import os

people = ['Cristiano Ronaldo', 'Lionel Messi', 'Neymar Junior', 'Robert Lewandowski', 'Dani Alves','Luka Modric','Kevin De Bruyne','Karim Benzema','Sergio Ramos', 'Luis Suarez']
DIR = r'C:\\Coding\\ML Practice\\CV2 practise\\photos'


# Creating the training set
haar_cascade = cv2.CascadeClassifier('haar_face.xml')
features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            img_array = cv2.imread(img_path)
            gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training Done!')
features = np.array(features)
labels = np.array(labels)

# Initiating the recognizer
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# train the recognizer on the featurs and labels
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy',labels)
