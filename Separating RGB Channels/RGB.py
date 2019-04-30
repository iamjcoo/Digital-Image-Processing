import cv2
import numpy as np 

im_file ="RGB_input.jpg"

img = cv2.imread(im_file,1)
img2 = cv2.imread(im_file,1)
img3 = cv2.imread(im_file,1)

# get image properties.
h, w, bpp = np.shape(img)

# iterate over the entire image and remove green and red channel.
for py in range(0, h):
    for px in range(0, w):
        img[py][px][1] = 0
        img[py][px][2] = 0

# display blue channel image
img = cv2.resize(img, (960, 540))   


# iterate over the entire image and remove blue and red channel.
for py in range(0, h):
    for px in range(0, w):
        img2[py][px][0] = 0
        img2[py][px][2] = 0

# display green channel image
img2 = cv2.resize(img2, (960, 540)) 



# iterate over the entire image and remove green and blue channel.
for py in range(0, h):
    for px in range(0, w):
        img3[py][px][0] = 0
        img3[py][px][1] = 0

# display red channel image
img3 = cv2.resize(img3, (960, 540)) 

cv2.imshow('Blue Channel', img)
cv2.imshow('Green Channel', img2)
cv2.imshow('Red Channel', img3)

cv2.waitKey(0)