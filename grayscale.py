import numpy as np 
import cv2 
import imutils

image = cv2.imread("testudo.jpg")

cv2.imshow("Original", image)

for x in range(0, image.shape[0]-1):
	for y in range(0, image.shape[1]-1):
		(b,g,r) = image[x,y]
		image[x,y] = (0.33*b + 0.33*g + 0.33*r)
cv2.imshow("Greyscale",image)
cv2.waitKey(0)