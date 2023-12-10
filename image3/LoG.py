import cv2
import numpy as np

pic_file = '..\HW4_test_image\image3.jpg'

img = cv2.imread(pic_file, 0)
row,col= img.shape

output = (img/255).copy()

log_out = cv2.copyMakeBorder(img, 2, 2, 2, 2,cv2.BORDER_CONSTANT, value=[255, 255, 255])

c = [  0.0, 0.0,-1.0 , 0.0, 0.0,
        0.0,-1.0,-2.0 ,-1.0, 0.0,
        -1.0,-2.0, 16.0,-2.0,-1.0,
        0.0,-1.0,-2.0 ,-1.0, 0.0,
        0.0, 0.0,-1.0 , 0.0, 0.0]
row =row+4
col =col+4
for i in range(2,row-3):
    for j in range(2,col-3):
        output[i-2][j-2] =c[0]  * log_out[i - 2][j - 2] + c[1]  * log_out[i - 2][j - 1] + c[2]  * log_out[i - 2][j] +c[3]  * log_out[i - 2][j + 1] + c[4]  * log_out[i - 2][j + 2] + \
                          c[5]  * log_out[i - 1][j - 2] + c[6]  * log_out[i - 1][j - 1] + c[7]  * log_out[i - 1][j] +c[8]  * log_out[i - 1][j + 1] + c[9]  * log_out[i - 1][j + 2] + \
                          c[10] * log_out[i    ][j - 2] + c[11] * log_out[i    ][j - 1] + c[12] * log_out[i    ][j] +c[13] * log_out[i    ][j + 1] + c[14] * log_out[i    ][j + 2] + \
                          c[15] * log_out[i + 1][j - 2] + c[16] * log_out[i + 1][j - 1] + c[17] * log_out[i + 1][j] +c[18] * log_out[i + 1][j + 1] + c[19] * log_out[i + 1][j + 2] + \
                          c[20] * log_out[i + 2][j - 2] + c[21] * log_out[i + 2][j - 1] + c[22] * log_out[i + 2][j] +c[23] * log_out[i + 2][j + 1] + c[24] * log_out[i + 2][j + 2]

numpy_horizontal = np.hstack((img/255, output/255))
cv2.imshow('Original v.s LoG',numpy_horizontal)
cv2.waitKey(0)
#cv2.imwrite('./image3/LoG.jpg',output)
