import cv2
import numpy as np

#Cascades
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

def detectFace(grayImg, originalImg):
    faces = face_cascade.detectMultiScale(grayImg, 1.3, 5)
    for(x,y,w,h) in faces:
        cv2.rectangle(originalImg, (x,y), (x+w, y+h), (255,0,0), 2)
    cv2.imshow("Object detection", img)          

def detectEyes(grayImg, originalImg):
    eyes = eye_cascade.detectMultiScale(grayImg, 1.3, 5)
    for(x,y,w,h) in eyes:
        cv2.rectangle(originalImg, (x,y), (x+w, y+h), (255,0,0), 2)
    cv2.imshow("Object detection", img)          
    cv2.imshow("Myface", grayImg)    

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detectFace(gray, img)
    detectEyes(gray, img)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

cap.release()
cv2.destroyAllWindows()
