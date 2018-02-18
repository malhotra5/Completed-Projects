import cv2
import numpy as np

glasses_cascade = cv2.CascadeClassifier("cascade.xml")

cap = cv2.VideoCapture(0)

def detectGlasses(grayImg, originalImg):
    glasses = glasses_cascade.detectMultiScale(grayImg,20,20)
    for(x,y,w,h) in glasses:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, "Glasses", (x-w, y-h), font, 0.5, (0,255,255), 2, cv2.LINE_AA)
        cv2.rectangle(originalImg, (x,y), (x+w, y+h), (255,0,0), 2)
    cv2.imshow("Object detection", img)


while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detectGlasses(gray, img)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
cap.release()

cv2.destroyAllWindows()

