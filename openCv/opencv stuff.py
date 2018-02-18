import numpy as np
import cv2
import matplotlib.pyplot as plt
#Importing in one color
img = cv2.imread("Spanish.jpg", cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR for color img
#IMREAD_ UNCHANGED to not change anything

#cv2.imshow("image", img) rgb
plt.imshow(img, cmap= "gray", interpolation= "bicubic")
#has to be gray as this one is brg
plt.show()
