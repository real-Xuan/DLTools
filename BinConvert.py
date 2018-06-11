import os
import cv2
import numpy as np
import time

save_dir = "D:/Desktop/WriteData/test/"
#file_dir = "D:/Desktop/WriteData/image/"
file_dir = "D:/Desktop/New_testdata/2/"

for file in os.listdir(file_dir):

    img = cv2.imread(file_dir + file)
    img = cv2.resize(img,(32, 32))
    if img is None:
        continue
    b = img[:,:,0].flatten()
    #print(b)
    g = img[:,:,1].flatten()
    #print(g)
    r = img[:,:,2].flatten()
    #print(r)
    label = [2]

    out = np.array(list(label) + list(r) + list(g) + list(b),np.uint8)
    print(out)
    out.tofile("D:/Desktop/WriteData/test/out.bin")

time.sleep(5)
    

print("All set!")