import cv2
import numpy as np

watch_cascade = cv2.CascadeClassifier("cascade.xml")
cap = cv2.VideoCapture(0)

def detectWatches(grayImg, originalImg):
    watches = watch_cascade.detectMultiScale(grayImg, 200, 200)
    for(x,y,w,h) in watches:
        cv2.rectangle(originalImg, (x,y), (x+w, y+h), (255,0,0), 2)
    cv2.imshow("Object detection", img)



while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detectWatches(gray, img)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

cap.release()
cv2.destroyAllWindows()
