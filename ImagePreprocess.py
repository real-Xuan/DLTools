import os
import cv2
import numpy as np


class ImagePreprocess:

    def __init__(self, path):
        self.inputDirectory = None
        self.outputDirectory = None

    def rgbAverage(self):

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

            eq = cv2.merge([eq_b, eq_g, eq_r])

            cv2.imwrite(root_path + "rgb_" + str(file), eq)

            print("Completed - " + str(n))

    def grayAverage(self):
        for file in os.listdir(file_dir):
            n += 1
            img = cv2.imread(file_dir + file, 0)
            if img is None:
                continue
            eq = cv2.equalizeHist(img)
            cv2.imwrite(root_path + str(file), eq)
            print("Image" + str(n))

    def grayWorld(self):
        nimg = nimg.transpose(2, 0, 1).astype(np.uint32)
        avgB = np.average(nimg[0])
        avgG = np.average(nimg[1])
        avgR = np.average(nimg[2])

        avg = (avgB + avgG + avgR) / 3

        nimg[0] = np.minimum(nimg[0] * (avg / avgB), 255)
        nimg[1] = np.minimum(nimg[1] * (avg / avgG), 255)
        nimg[2] = np.minimum(nimg[2] * (avg / avgR), 255)
        return nimg.transpose(1, 2, 0).astype(np.uint8)

    def imageToBin(self):
        img = cv2.imread(file_dir + file)
        img = cv2.resize(img, (32, 32))
        if img is None:
            pass
        b = img[:, :, 0].flatten()
        # print(b)
        g = img[:, :, 1].flatten()
        # print(g)
        r = img[:, :, 2].flatten()
        # print(r)
        label = [2]

        out = np.array(list(label) + list(r) + list(g) + list(b), np.uint8)
        print(out)
        out.tofile("D:/Desktop/WriteData/test/out.bin")
