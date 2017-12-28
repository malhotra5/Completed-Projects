import cv2
import numpy as np

img1 = cv2.imread("image1.jpg")
img2 = cv2.imread("image2.jpg")
imposeImg = cv2.imread("background1.jpg")
#Adds images over each other
#add = img1 + img2

#Adds pixel values
##add = cv2.add(img1,img2)

#Weighted add to specify how much weight each image gets (opaqueness) 
##weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)


rows , cols, channels = imposeImg.shape
roi = img1[0:rows, 0:cols]

main2gray = cv2.cvtColor(imposeImg, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(main2gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
main_fg = cv2.bitwise_and(imposeImg, imposeImg, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dist

cv2.imshow("added nicely", img1)
cv2.imshow("Image1", img1)
cv2.imshow("Image2", img2)
cv2.imshow("IMPOSING", imposeImg)
##cv2.imshow("BOTH", add)
##cv2.imshow("WEIGHTED", weighted)

cv2.waitKey(0)
cv2.destroyAllWindows()
