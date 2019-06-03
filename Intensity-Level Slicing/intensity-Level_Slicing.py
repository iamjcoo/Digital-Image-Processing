import cv2
import numpy as np 

im_file ="moon.jpg"
img = cv2.imread(im_file,1)


# get image properties.
h, w, bpp = np.shape(img)

# iterate over the entire image and convert to Grayscale.
for py in range(0, h):
    for px in range(0, w):
        if img[py][px][0] >= 100 and img[py][px][0] <=200:
                img[py][px][0]=255
                img[py][px][1]=255
                img[py][px][2]=255
        else:
                img[py][px][0]=0
                img[py][px][1]=0
                img[py][px][2]=0

cv2.imwrite('moon_output.jpg',img)