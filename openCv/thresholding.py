import cv2
import numpy as np
#Threshold on normal pic
img = cv2.imread("Spanish.jpg")
retval, threshold = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)
#Threshhold on grey pic
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grey, 220, 255, cv2.THRESH_BINARY)
#Adaptive threshold for better view
gaus = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)


cv2.imshow("ORIGINAL", img)
cv2.imshow("THRESHED", threshold)
cv2.imshow("THRESHED2", threshold2)
cv2.imshow("ADAPTIVE", gaus)

cv2.waitKey(0)
cv2.destroyAllWindows()
