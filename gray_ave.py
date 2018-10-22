import os
import cv2

root_path = "/Users/zx/Desktop/image/save/"
file_dir = "/Users/zx/Desktop/image/"
n = 0

for file in os.listdir(file_dir):
	n += 1
	img = cv2.imread(file_dir + file, 0)
	if img is None:
		continue
	eq = cv2.equalizeHist(img)
	cv2.imwrite(root_path + str(file), eq)
	print("Image" + str(n))
	
	
