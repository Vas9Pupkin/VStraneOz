import cv2
import Volwebnik
img_path =Volwebnik.Opening()
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
print(img.shape)
img [100:-99,100:-99] = 0
out_path = Volwebnik.Soxrani()
cv2.imwrite(out_path, img)