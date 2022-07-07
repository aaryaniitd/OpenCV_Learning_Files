# Code to rescale/resize a frame/image

import cv2
# img = cv2.imread('C:\\Coding\\ML Practice\\CV2 practise\\photos\\ney.png') #reads the image
# cv2.imshow('Ney', img)

def rescaleFrame(frame, scale=1.2):
    # this function works for images, videos and live videos

    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)
    
def changeRes(width, height):
    # works on live video only
    capture.set(3,width)
    capture.set(4,height)


capture = cv2.VideoCapture(0) # if the input is int then it will open webcam or if path is given then it will take a video
while True:
    isTrue, frame = capture.read() #capture reads every frame of the video
    frame_resized= rescaleFrame(frame)
    cv2.imshow('Video Resized',frame_resized)

    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
