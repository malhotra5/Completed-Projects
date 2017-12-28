import cv2
import numpy as np

img = cv2.imread("Spanish.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread("Match.jpg", 0)
w, h = template.shape[::-1]



res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (255, 0 ,0), 2)

cv2.imshow("Original", img)
cv2.imshow("Template", template)
