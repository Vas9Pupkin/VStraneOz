import cv2
import Volwebnik
img_path =Volwebnik.Opening()
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
print(img.shape)
img[0:,0:50],img[0:50,0:],img[0:,-50:],img[-50:,0:] = 0,0,0,0
img[0+50:-49,0+50:50+50],img[0+50:50+50,0+50:-49],img[0+50:-49,-50-50:-49],img[-50-50:-49,0+50:-49] = 255,255,255,255
out_path = Volwebnik.Soxrani()
cv2.imwrite(out_path, img)