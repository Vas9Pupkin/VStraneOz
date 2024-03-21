import cv2
import numpy as np
import Volwebnik
from Pygalo import max_functin, min_functin, VdolbNochnixDorog
import copy
ssilka=Volwebnik.Opening()
input_img =cv2.imread(ssilka)
kernel1=np.ones((3,3))/9
kernel2=np.array([[1,2,1],[2,4,2],[1,2,1]])/16
ssilka_2,ssilka_3,ssilka_4,ssilka_5,ssilka_6=Volwebnik.Soxrani(),Volwebnik.Soxrani(),Volwebnik.Soxrani(),Volwebnik.Soxrani(),Volwebnik.Soxrani()
out_img2 = cv2.filter2D(input_img,-1,kernel1)
out_img3 = cv2.filter2D(input_img,-1,kernel2)
out_img4 = cv2.medianBlur(input_img, 9)
# max_img = max_functin(3, 3, copy.copy(input_img))
# min_img=min_functin(3, 3, copy.copy(input_img))
max_img, min_img=VdolbNochnixDorog(copy.copy(input_img))
cv2.imwrite(ssilka_2, out_img2)
cv2.imwrite(ssilka_3, out_img3)
cv2.imwrite(ssilka_4, out_img4)
cv2.imwrite(ssilka_5, min_img)
cv2.imwrite(ssilka_6, max_img)
# Работает, но долго, лучше 14 15 строки, но пк не тянет, 16 строка хуже, но даже она 15 минут делалась? проверить работу лучше через маленькую фотографию