import cv2
import numpy as np
import math

def generate_kernel():
    size = 15
    # generating the kernel
    kernel_motion_blur = np.zeros((size, size))
    kernel_motion_blur[int((size-1)/2), :] = np.ones(size)
    kernel = kernel_motion_blur / size

    return kernel

def genarate_Psf(length,angle):
    EPS=np.finfo(float).eps                                 
    alpha = (angle-math.floor(angle/ 180) *180) /180* math.pi
    cosalpha = math.cos(alpha)  
    sinalpha = math.sin(alpha)
    half = length / 2
    if cosalpha < 0:
        xsign = -1
    elif angle == 90:
        xsign = 0
    else:  
        xsign = 1
    psfwdt = 1;  

    sx = int(math.fabs(length*cosalpha + psfwdt*xsign - length*EPS))  
    sy = int(math.fabs(length*sinalpha + psfwdt - length*EPS))
    psf1=np.zeros((sy,sx))
     

    for i in range(0,sy):
        for j in range(0,sx):
            psf1[i][j] = i*math.fabs(cosalpha) - j*sinalpha
            rad = math.sqrt(i*i + j*j) 
            if  rad >= half and math.fabs(psf1[i][j]) <= psfwdt:  
                temp = half - math.fabs((j + psf1[i][j] * sinalpha) / cosalpha)  
                psf1[i][j] = math.sqrt(psf1[i][j] * psf1[i][j] + temp*temp)
            psf1[i][j] = psfwdt + EPS - math.fabs(psf1[i][j]);  
            if psf1[i][j] < 0:
                psf1[i][j] = 0

    anchor=(0,0)

    if angle<90 and angle>0:
        psf1=np.fliplr(psf1)
        anchor=(psf1.shape[1]-1,0)
    elif angle>-90 and angle<0:
        psf1=np.flipud(psf1)
        psf1=np.fliplr(psf1)
        anchor=(psf1.shape[1]-1,psf1.shape[0]-1)
    elif anchor<-90:
        psf1=np.flipud(psf1)
        anchor=(0,psf1.shape[0]-1)
    
    psf1=psf1/psf1.sum()
    
    return psf1,anchor

    
def main(argv=None):
    kernel, anchor = genarate_Psf(50, 0.1)
    print(kernel)
    img = cv2.imread('D:/Desktop/WriteData/image/2.jpg')
    cv2.imshow('Original', img)
    output = cv2.filter2D(img, -1, kernel, anchor=anchor)
    cv2.imshow('Motion Blur', output)
    cv2.imwrite("D:/Desktop/WriteData/image/blur2.jpg", output)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
