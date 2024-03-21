import numpy as np
import cv2
import Volwebnik
a=cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (512, 512))
b=cv2.getStructuringElement(cv2.MORPH_CROSS, (512, 512))
a[:,:]*=255
b[:,:]*=255
print('Save Elli')
cv2.imwrite(Volwebnik.Soxrani(),a)
print('Save Krest')
cv2.imwrite(Volwebnik.Soxrani(),b)