#Sketching your webcam using OpenCV and Python
import os
import numpy as np
import cv2

def sketch(image):
    img_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    img_blur=cv2.GaussianBlur(img_gray,(3,3),0)
    edges=cv2.Canny(img_blur,10,80)
    ret,mask=cv2.threshold(edges,50,255,cv2.THRESH_BINARY_INV)
    
    return mask
#Capturing video from web cam
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    cv2.imshow('Live_Sketch',sketch(frame))
    # Key13==ENTER_KEY
    if cv2.waitKey(1)==13:
        break
# releasing_webcam
cap.release()
# destroying_window
cv2.destroyAllWindows()
    






