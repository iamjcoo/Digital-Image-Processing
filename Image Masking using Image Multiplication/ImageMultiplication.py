import cv2
import numpy as np 

im_file1 ="Fig0230a.tif"
im_file2 ="Fig0230b.tif"

img = cv2.imread(im_file1,1)
img2 = cv2.imread(im_file2,1)
output = cv2.imread(im_file1,1)

# get image properties.
h1, w1, bpp1 = np.shape(img)

# iterate over the entire image and add create filled box.
for py in range(0, h1):
    for px in range(0, w1):
        cval = img[py][px][0] * (img2[py][px][0] / 255)
        output[py][px][0] = cval
        output[py][px][1] = cval
        output[py][px][2] = cval

# display red channel image
img = cv2.resize(output, (882, 674)) 

cv2.imwrite('output.jpg', output)
cv2.waitKey(0)