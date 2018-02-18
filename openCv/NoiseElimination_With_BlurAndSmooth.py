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

    #Loosing background noise with different types of filter
    kernel = np.ones((15,15), np.float32)/255
    smoothed = cv2.filter2D(res, -1, kernel)
    blur = cv2.GaussianBlur(res, (15,15), 0)
    #Better clarity
    median = cv2.medianBlur(res, 15)
    
    ##cv2.imshow("Dectect and Filter", frame)
    ##cv2.imshow("Mask", mask)
    cv2.imshow("Result", res)
    cv2.imshow("Smoothed", smoothed)
    cv2.imshow("Blurred", blur)
    cv2.imshow("Median", median)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    

cv2.destroyAllWindows()
cap.release()
