import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    #hsv - hue, saturation and value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    ##Horror film
    ##lower_blue = np.array([50,0,0])
    ##upper_blue = np.array([255,255,255])

    lower_yellow = np.array([29,97,0])
    upper_yellow = np.array([66,255,255])

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    
    cv2.imshow("Dectect and Filter", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", res)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    

cv2.destroyAllWindows()
cap.release()
