import cv2
import numpy as np 

img = cv2.imread("sample.jpg",1)
# get image properties.
h, w, bpp = np.shape(img)

# iterate over the entire image.
for py in range(0, h):
    for px in range(0, w):
        img[py][px][1] = 0
        img[py][px][2] = 0

# display image
cv2.imwrite('im1.png',img)

# iterate over the entire image.
for py in range(0, h):
    for px in range(0, w):
        img[py][px][0] = 0
        img[py][px][2] = 0

# display image
cv2.imwrite('im2.png',img)

# iterate over the entire image.
for py in range(0, h):
    for px in range(0, w):
        img[py][px][0] = 0
        img[py][px][1] = 0

# display image
cv2.imwrite('im3.png',img)