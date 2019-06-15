# *********************************************************************
# filename : Onate_ShCircle.py
# subject : Digital Image Processing
# semester : Summer Class 2019
# 
#
# Solution:
# 1. read the image file 
# 2. open coordinates file and save it to object f
# 3. iterate over to every line of the file
# 4. check if line is equal to 0 then continue or check whether line is empty 
# 5. otherwise get the content and get the coordinates of A, B, C, D, E
# 7. iterate over coordinates and check the color of the coordinates and its neighbor and save it to colorl list. 
# 8. get the average of the list of color and save it to color variable
# 9. if color variable is less than 150, red rectangle border will be drawn on the coordinates, otherwise, green rectangle border will be drawn on the coordinates
# 10. final image will be shown
# *********************************************************************


import cv2
import numpy as np

img = cv2.imread('input/3.jpg', 1)
f = open("coordinates.txt", "r")
i=0
for point in f:
    if i==0:
        i+=1
        continue
    elif point=="":
        continue
    else:
        my_list = point.split()
        for point2 in my_list:
            tpoint = point2.split(",")
            colorl=[]
            for x in range(10):
                colorl.append(img[int(tpoint[0])-x, int(tpoint[1])-x][0])
                colorl.append(img[int(tpoint[0])+x, int(tpoint[1])+x][0])
            color = sum(colorl)/len(colorl)
            if(color<150):
                cv2.rectangle(img, (int(tpoint[1])-15, int(tpoint[0])-15), (int(tpoint[1])+15, int(tpoint[0])+15), (0,0,255), 2)
            else:
                cv2.rectangle(img, (int(tpoint[1])-15, int(tpoint[0])-15), (int(tpoint[1])+15, int(tpoint[0])+15), (34,139,34), 2)
        my_list = []

cv2.imwrite('output.jpg', img)
cv2.waitKey(0)
