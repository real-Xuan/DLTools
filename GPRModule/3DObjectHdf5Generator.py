import h5py
import numpy as np
import cv2

def imageBinarization():
    image = cv2.imread('/Users/Xuan/Developer/DLTools/images/root.jpg', 0)
    cv2.threshold(image, 200, 255, cv2.THRESH_BINARY, image)
    cv2.imwrite('/Users/Xuan/Developer/DLTools/images/root_binary.jpg', image)

#return [0,1) random 3d array
def random3dArray():
    return np.random.random_sample(size=(64, 64, 64))

#write HDF5 file
# f = h5py.File('my_object.h5','w')
# dx_dy_dz = (0.005, 0.005, 0.005)
# data = cone()
# data = np.array(data,dtype=np.float16)
# f.attrs['dx_dy_dz'] = dx_dy_dz
# f['/data'] = data
