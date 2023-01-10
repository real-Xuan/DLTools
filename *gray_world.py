#https://www.cnblogs.com/wangyong/p/9119394.html

import os

import cv2
import numpy as np


def grey_world(nimg):  
   nimg = nimg.transpose(2, 0, 1).astype(np.uint32)  
   avgB = np.average(nimg[0])  
   avgG = np.average(nimg[1])  
   avgR = np.average(nimg[2])  
 
   avg = (avgB + avgG + avgR) / 3  
 
   nimg[0] = np.minimum(nimg[0] * (avg / avgB), 255)  
   nimg[1] = np.minimum(nimg[1] * (avg / avgG), 255)  
   nimg[2] = np.minimum(nimg[2] * (avg / avgR), 255)  
   return  nimg.transpose(1, 2, 0).astype(np.uint8)
   
root_path = "D:/Desktop/2018-6-12_Eyeblink_data_gray-world_test/random/"
file_dir = "D:/Desktop/2018-6-11_Eyeblink_data/EyeBlinkDB_Test/random/"
n = 0

for file in os.listdir(file_dir):
    n += 1
    img = cv2.imread(file_dir + file)
    if img is None:
        continue
        
    eq = grey_world(img)
    
    cv2.imwrite(root_path + "grayworld_" + str(file), eq)
