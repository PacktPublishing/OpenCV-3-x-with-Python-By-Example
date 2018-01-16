import cv2

img = cv2.imread('./images/input.jpg')
cv2.imshow('Input image', img)

cv2.waitKey()