import cv2
import numpy as np 

im_file ="inputcolor.jpg"
img = cv2.imread(im_file,1)
img2 = cv2.imread(im_file,1)
threshold = 113
maxv=0
# get image properties.
h, w, bpp = np.shape(img)

# iterate over the entire image and convert to Grayscale.
for py in range(0, h):
    for px in range(0, w):
        ave = (int(img[py][px][0]) + int(img[py][px][1]) + int(img[py][px][2])) / 3
        img[py][px][0] = ave
        img[py][px][1] = ave
        img[py][px][2] = ave
        if ave > maxv:
            maxv = ave

#setting threshold
threshold = int(maxv / 2)
# iterate over the entire grayscale image and convert to Binary.
for py in range(0, h):
    for px in range(0, w):
        if img[py][px][0] > threshold: 
            img2[py][px][0] = 255
            img2[py][px][1] = 255
            img2[py][px][2] = 255
        else: 
            img2[py][px][0] = 0
            img2[py][px][1] = 0
            img2[py][px][2] = 0


img = cv2.resize(img, (1024, 512)) 
img2 = cv2.resize(img2, (1024, 512)) 

cv2.imwrite('grayscale.jpg',img)
cv2.imwrite('binary.jpg',img2)