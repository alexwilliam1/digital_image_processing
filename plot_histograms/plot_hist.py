import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('ph2_original.png')
img2 = cv2.imread('ph2_histEq.png')

plt.hist(img.ravel(), 256, [1, 256])
plt.hist(img2.ravel(), 256, [1, 256])

plt.legend(['Imagem original', 'Equalizacao do Histograma'])
plt.show()
