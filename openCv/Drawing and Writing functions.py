import numpy as np
import cv2

img = cv2.imread("Spanish.jpg", cv2.IMREAD_COLOR)
cv2.line(img, (0,0), (150,150), (255,0,0), 15)#BGR image,coordinates2, color, width

#cv2.rectangle(img, (15,25), (150,150), (255,0,0), 15)#image, coordinates2, color, width

#Joining bunch of dots to a polygon
points = np.array([[15,20], [20,30], [70,50], [50,10]], np.int32) #npint32 - numpy int type
#points  = points.reshape((-1,1,2)) reshapes points
cv2.polylines(img, [points], True, (0,255,255), 10)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "THIS IS VICKY!", (30,130), font, 1, (0,0,0), 2, cv2.LINE_AA)


cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

