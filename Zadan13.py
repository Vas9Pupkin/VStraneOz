import cv2
import numpy as np
from skimage import restoration
import matplotlib.pyplot as plt
import Volwebnik
img =cv2.imread(Volwebnik.Opening(),cv2.IMREAD_GRAYSCALE)/255
kernel = np.ones((7, 7)) / (49)
img_blur=np.random.normal(img,scale=0.15,size=img.shape)
#img_blur=cv2.GaussianBlur(img,(7,7),0)
deconvolved_RL =restoration.richardson_lucy(img_blur, kernel,num_iter=30)
fig, ax = plt.subplots(nrows=1, ncols=3,
figsize=(8, 5))
plt.gray()
for a in (ax[0], ax[1], ax[2]):
    a.axis('off')
ax[0].imshow(img)
ax[0].set_title('Оригинальное изображение')
ax[1].imshow(img_blur)
ax[1].set_title('Размытое \n изображение')
ax[2].imshow(deconvolved_RL)
ax[2].set_title('Восстановленное \n изображение')
fig.subplots_adjust(wspace=0.02, hspace=0.2,top=0.9, bottom=0.05, left=0,right=1)
plt.show()