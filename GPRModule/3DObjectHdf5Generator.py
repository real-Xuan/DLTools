import os
import numpy as np
import cv2

def imageBinarization():
# TODO: More general way to do this
    image = cv2.imread('/Users/Xuan/Developer/DLTools/images/root.jpg', 0)
    cv2.threshold(image, 200, 255, cv2.THRESH_BINARY, image)
    cv2.imwrite('/Users/Xuan/Developer/DLTools/images/root_binary.jpg', image)

def png2Hdf5():
    os.system('python -m tools.convert_png2h5 root_binary_part.png 0.002 0.002 0.002 -zcells 150')