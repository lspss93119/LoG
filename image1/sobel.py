import cv2
import numpy as np
pic_file = '..\HW4_test_image\image1.jpg'

img = cv2.imread(pic_file, 0)
row,col= img.shape


c=[(-1,-2,-1,0,0,0,1,2,1), (-1,0,1,-2,0,2,-1,0,1)]

so = (img/255).copy()

for i in range(0,row-1):
    for j in range(0,col-1):
            type = 0
            x =   c[type][0] * img[i - 1][j - 1]  + c[type][1] * img[i - 1][j]   + c[type][2] * img[i - 1][j + 1]+\
                   c[type][3] * img[i    ][j - 1]  + c[type][4] * img[i    ][j]   + c[type][5] * img[i    ][j + 1]+\
                  c[type][6] * img[i + 1][j - 1]  + c[type][7] * img[i + 1][j]   + c[type][8] * img[i + 1][j + 1]
            type = 1
            y =   c[type][0] * img[i - 1][j - 1]  + c[type][1] * img[i - 1][j]   + c[type][2] * img[i - 1][j + 1]+\
                  c[type][3] * img[i    ][j - 1]  + c[type][4] * img[i    ][j]   + c[type][5] * img[i    ][j + 1]+\
                  c[type][6] * img[i + 1][j - 1]  + c[type][7] * img[i + 1][j]   + c[type][8] * img[i + 1][j + 1]
            so[i][j] = (x**2+y**2)**0.5

numpy_horizontal = np.hstack((img/255, so/255))
cv2.imshow('Original v.s sobel',numpy_horizontal)
cv2.waitKey(0)
#cv2.imwrite('./image1/sobel.jpg',so)
