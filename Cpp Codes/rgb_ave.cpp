#include <iostream>  
#include <opencv2/core/core.hpp>  
#include <opencv2/highgui/highgui.hpp>  
#include <iostream>
#include <stdio.h>
#include <stdlib.h>

#include "cv.h"
#include "highgui.h"

using namespace cv;
using namespace std;

void main( ){	//rgb直方图均衡化处理
	//开始rgb三通道直方图均衡化

	Mat image = imread("D:\\Desktop\\tmp\\10.png", CV_LOAD_IMAGE_UNCHANGED);

	Mat mergeImg;//合并后的图像  
	//用来存储各通道图片的向量  
	vector<Mat> splitBGR(image.channels());
	//分割通道，存储到splitBGR中  
	split(image, splitBGR);
	//对各个通道分别进行直方图均衡化  
	for (int i = 0; i < image.channels(); i++)
		equalizeHist(splitBGR[i], splitBGR[i]);
	//合并通道  
	merge(splitBGR, mergeImg);
	image = mergeImg;

	imwrite("D:\\Desktop\\tmp\\temp.png", image);
}
