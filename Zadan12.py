import cv2
import numpy as np
from scipy.signal import convolve2d
from skimage import restoration
import matplotlib.pyplot as plt
import Volwebnik
img =cv2.imread(Volwebnik.Opening(),cv2.IMREAD_GRAYSCALE)/255
kernel = np.ones((11, 11)) / (121)
img_blur = convolve2d(img, kernel, 'same')
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
#Другой kernel
kernel2 = np.ones((3, 3)) / 9
img_blur2 = convolve2d(img, kernel2, 'same')
deconvolved_RL2 =restoration.richardson_lucy(img_blur2, kernel2,num_iter=30)
fig2, ax2 = plt.subplots(nrows=1, ncols=3,
figsize=(8, 5))
plt.gray()
for a in (ax2[0], ax2[1], ax2[2]):
    a.axis('off')
ax2[0].imshow(img)
ax2[0].set_title('Оригинальное изображение')
ax2[1].imshow(img_blur2)
ax2[1].set_title('Размытое \n изображение')
ax2[2].imshow(deconvolved_RL2)
ax2[2].set_title('Восстановленное \n изображение')
fig2.subplots_adjust(wspace=0.02, hspace=0.2,top=0.9, bottom=0.05, left=0,right=1)
plt.show()