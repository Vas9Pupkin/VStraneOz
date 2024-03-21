import numpy as np
import cv2
import Volwebnik
a=cv2.imread(Volwebnik.Opening(), cv2.IMREAD_GRAYSCALE)
kernel, kernel2=np.ones((3,3)), np.ones((5,5))
r1=cv2.dilate(a,kernel)
r2=cv2.erode(a,kernel)
r3=cv2.dilate(a,kernel2)
r4=cv2.erode(a,kernel2)
cv2.imshow('Dilat1', r1)
cv2.imshow('Er1', r2)
cv2.imshow('Dilat2', r3)
cv2.imshow('Er2', r4)
cv2.imwrite(Volwebnik.Soxrani(),r1)
cv2.imwrite(Volwebnik.Soxrani(),r2)
cv2.imwrite(Volwebnik.Soxrani(),r3)
cv2.imwrite(Volwebnik.Soxrani(),r4)
cv2.waitKey(0)