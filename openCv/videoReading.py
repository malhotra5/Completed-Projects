import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("iLikeIt.avi", fourcc, 20.0, (640,480))
while True:
    ret, frame  = cap.read()
    cv2.imshow("frame", frame)
    out.write(frame)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) convert to grey image
    #cv2.imshow("gray image", gray) showing grey image
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()
