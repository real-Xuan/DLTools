#coding=utf-8  

import os
import cv2
import time

root_path = "D:/Desktop/2018-6-11_Eyeblink_data_rgb+ave_test/random/"
file_dir = "D:/Desktop/2018-6-11_Eyeblink_data/EyeBlinkDB_Test/random/"
n = 0

for file in os.listdir(file_dir):
    n += 1
    img = cv2.imread(file_dir + file)
    if img is None:
        continue
        
    b = cv2.split(img)[0]
    g = cv2.split(img)[1]
    r = cv2.split(img)[2]
    
    eq_b = cv2.equalizeHist(b)
    eq_g = cv2.equalizeHist(g)
    eq_r = cv2.equalizeHist(r)
    
    eq = cv2.merge([eq_b,eq_g,eq_r])
    
    cv2.imwrite(root_path + "rgb_" + str(file), eq)
    
    print("Completed - " + str(n))

time.sleep(5)
    

print("All set!")