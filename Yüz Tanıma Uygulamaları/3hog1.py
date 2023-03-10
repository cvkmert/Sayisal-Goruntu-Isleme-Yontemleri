# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 12:06:56 2023

@author: cvkme
"""

from skimage.io import imread, imshow
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt
#☺%matplotlib inline

img = imread("images/elon_musk.jpg")
imshow(img)
print(img.shape)

resized_img = resize(img(128, 64))
imshow(resized_img)
print(resized_img.shape)

fd, hog_image = hog(resized_img, orientations=9, pixels_per_cell=(8,8),
                    cells_per_block=(2,2), visualize=True, multichannel=True)

fig, (ax1, ax2) =plt.subplots(1, 2, figsize=(16, 8), sharex=True, sharey=True)

ax1.imshow(resized_img, cmap=plt.cm.gray)
ax1.set_title("Girilen Resim")

hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
ax2.set_title("Yönlendirilmiş Histogram")

plt.show()