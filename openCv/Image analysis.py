import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Spanish.jpg", cv2.IMREAD_COLOR)

#Color value for the pixel px on image "img"
px = img[55,55]
#Changing pixel color
#img[55,55] = [255,255,255]
#ROI - Reigon of Image
#roi = img[100:150, 100:150] numpy arrary for a reigon on img


##plt.imshow(img, cmap = "gray", interpolation = "bicubic")
##plt.show()

my_face = img[273:85, 409:260]
img[0:0, 0:0] = my_face

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

