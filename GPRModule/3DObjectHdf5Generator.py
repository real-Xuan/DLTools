import h5py
import numpy as np

def cone(r=1):
    a = np.full([64,64,64],1)
    for c in range(64):
        for i in range(64):
            for j in range(64):
                if (i - 32) ** 2 + (j - 32) ** 2 < r:
                    a[i][j][c] = 0
        r += 1
    return a

#return [0,1) random 3d array
def random3dArray():
    return np.random.random_sample(size=(64, 64, 64))

#write HDF5 file
f = h5py.File('my_object.h5','w')
dx_dy_dz = (0.005, 0.005, 0.005)
data = cone()
data = np.array(data,dtype=np.int16)
f.attrs['dx_dy_dz'] = dx_dy_dz
f['/data'] = data
