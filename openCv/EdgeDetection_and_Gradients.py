import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    ##Gradient grapher
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 5)

    #Edge detectors
    edges = cv2.Canny(frame, 100, 50)
    
    cv2.imshow("Original", frame)
    cv2.imshow("laplacian", laplacian)
    cv2.imshow("Soblex", sobelx)
    cv2.imshow("Sobely", sobely)
    cv2.imshow("Edge Detection", edges)
            
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break


cv2.destroyAllWindows()
cap.release()
