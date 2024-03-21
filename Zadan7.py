import cv2
import Volwebnik
img_path =Volwebnik.Opening()
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
print(img.shape)
for i in range (img.shape[0]):
    for j in range (img.shape[1]):
        if img[i][j]<75:
            img[i][j]=255
out_path = Volwebnik.Soxrani()
cv2.imwrite(out_path, img)
#Можно поискать оптимальное число от 50-125 +- (у меня 75), у меня делается секунд 30-40, так что оставлю так