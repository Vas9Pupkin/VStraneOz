import cv2
import numpy as np
import Volwebnik
ssilka=Volwebnik.Opening()
input_img =cv2.imread(ssilka)
kernel=np.ones((51,51))/(51*51)
out_img = cv2.medianBlur(input_img, 51)
out_img2 = cv2.filter2D(input_img,-1,kernel)
ssilka_2,ssilka_3=Volwebnik.Soxrani(),Volwebnik.Soxrani()
cv2.imwrite(ssilka_2, out_img)
cv2.imwrite(ssilka_3, out_img2)