import cv2
import numpy as np 

im_file1 ="Input1.png"
im_file2 ="Input2.png"

img = cv2.imread(im_file1,1)
img2 = cv2.imread(im_file2,1)
output = cv2.imread(im_file1,1)

# get image properties.
h1, w1, bpp1 = np.shape(img)

# iterate over the entire image and detect change in pixels.
for py in range(0, h1):
    for px in range(0, w1):
        cval = img[py][px][0] - img2[py][px][0]
        cval=abs(int(cval))
        if cval>=215:
            cval=0
        output[py][px][0] = cval
        output[py][px][1] = cval
        output[py][px][2] = cval

cv2.imwrite('SampleOutput.jpg', output)
cv2.waitKey(0)