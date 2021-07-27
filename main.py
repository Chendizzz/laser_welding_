import cv2
import numpy as np
import os
import struct
import matplotlib.pyplot as plt
from bmp_processing import twoBytes2_565
from bmp_processing import generateRGB_channel
from bmp_processing import preprocessing

dir_path_list = []
for dirpath, dirname, filename in os.walk("/Users/chendi/Downloads/2000p500n/NOK/NOK_50"):
    #(dirname)
    dir_path_list.append(str(dirpath))

dir_path_list = dir_path_list[1:]
for dir_ in dir_path_list:
    for file in os.listdir(dir_):
        if file.split('.')[-1] == 'bmp':
            f = open(dir_+"/"+file, 'rb')   #只读，二进制打开，if file.split(".")[-1] == "bmp":
            preprocessing(f)
            r, g, b = generateRGB_channel(f)
            rec_img = cv2.merge((r, g, b))
            rec_np_array = np.array(rec_img)[122:185, 0:4200]
            cv2.imwrite("imgs" + "/" + dir_.split('/')[-1] + '_'+file, rec_np_array)


        """
        f = open("raw_imgs/raw_NOK_imgs"+"/"+file, 'rb')  # 只读，二进制打开，
        preprocessing(f)
        r, g, b = generateRGB_channel(f)
        rec_img = cv2.merge((r, g, b))
        rec_np_array = np.array(rec_img)
        cv2.imwrite("imgs"+"/"+"rec_"+file, rec_np_array)
        print(rec_np_array.shape)
        #cv2.imshow("rec_img", rec_img)
        #cv2.waitKey(0)
        
        """


