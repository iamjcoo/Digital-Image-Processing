import cv2
import numpy as np 

im_file ="input.jpg"

img = cv2.imread(im_file,1)
img2 = cv2.imread(im_file,1)
# get image properties.
h, w, bpp = np.shape(img)

#setting boundaries
w4 = int(w/4)
h3 = int(h/3)
maxh = int(h3+h3)
maxw = int(w4*3)

# iterate over the entire image and add red border.
for py in range(0, h):
    for px in range(0, w):
        if (px > w4 and py > h3) and (px < maxw and py < maxh):
                img[py][px][0] = 0
                img[py][px][1] = 0
                img[py][px][2] = 255

for py in range(0, h):
    for px in range(0, w):
        if ((py >= h3 and py <= maxh)and(px>=w4 and px<=maxw)):
                if((py >= h3 and py <= (h3+10)) or (py>= (maxh-10) and py<=maxh)):
                        img2[py][px][0] = 0
                        img2[py][px][1] = 0
                        img2[py][px][2] = 255
                if(px>=w4 and px<=w4+10) or (px>=maxw-10 and px<=maxw):
                        img2[py][px][0] = 0
                        img2[py][px][1] = 0
                        img2[py][px][2] = 255      

# display red channel image
img = cv2.resize(img, (960, 640)) 
img2 = cv2.resize(img2, (960, 640)) 

cv2.imwrite('output1.jpg', img2)
cv2.imwrite('output2.jpg', img)
cv2.waitKey(0)