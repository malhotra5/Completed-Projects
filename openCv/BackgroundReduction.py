import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#Background reductor
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    #Background reduction for frame
    fgmask = fgbg.apply(frame)
    #Filtering noise
    kernel = np.ones((5,5), np.uint8)
    opening = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Original", frame)
    cv2.imshow("background reduced", closing)
    

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release
cv2.destroyAllWindows()
