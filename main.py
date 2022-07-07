# Code on how to display an image or a video

import cv2
# img = cv2.imread('C:\\Coding\\ML Practice\\CV2 practise\\photos\\ney.png') #reads the image
# cv2.imshow('N',img)
 
# cv2.waitKey(0) this means the time in microseconds for which the image is displayed until a key is pressed '0' means infinte time


#Reading Video
capture = cv2.VideoCapture(0) # if the input is int then it will open webcam or if path is given then it will take a video
while True:
    isTrue, frame = capture.read() #capture reads every frame of the video
    cv2.imshow('Video',frame)

    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
