#include<seeta/FaceDetector2.h>
#include<seeta/PointDetector2.h>
#include<seeta/FaceRecognizer.h>
#include<opencv2/opencv.hpp>
#include<seeta/Struct_cv.h>
#include<iostream>
#include<io.h>
#include<string>
#include<vector>

using namespace std;
using namespace cv;



void main()
{
	vector<Mat> read_images_in_folder(cv::String pattern);
	string path = "F:/taobao1thDBreal_black/07/real/0207/right/xl_";
	int k = 243;
	while (true)
	{
		string F_path = path + to_string(k);
		cout << F_path << endl;
		cv::String pattern = F_path;
		//cv::String pattern = "F:/taobao1thDBreal_black/07/real/0207/right/xl_";
		vector<Mat> images = read_images_in_folder(pattern);
		k = k + 1;
		
	}
	
}

std::vector<Mat> read_images_in_folder(cv::String pattern)
{
	vector<cv::String> fn;
	glob(pattern, fn, false);
	cout << "pattern"<<pattern << endl;
	vector<Mat> images;
	size_t count = fn.size();
	cout << count << endl;
	double s = 20;
	int pick_img = 0;
	for (size_t i = 0; i < count; i++)
	{
		Mat frame = imread(fn[i]);
		if (!frame.data)
		{
			continue;
		}
		images.push_back(frame);
		//imshow("img", imread(fn[i]));

		seeta::FaceDetector2 FD("bindata/SeetaFaceDetector2.0.ats");

		seeta::cv::ImageData image = frame;

		seeta::PointDetector2 PD("bindata/SeetaPointDetector2.0.pts5.ats");
		int num;
		SeetaRect *face = FD.Detect(image, &num);
		if (num==0)
		{
			continue;
		}
		SeetaPointF *points = PD.Detect(image, *face);
		/*
		if (points)
		{
			std::cout << "Points: [" << std::endl;
			for (int j = 0; j < PD.LandmarkNum(); ++j)
			{
				std::cout << "(" << points[j].x << ", " << points[j].y << ")," << std::endl;
			}
			std::cout << "]" << std::endl;
		}
		*/

		double result = 2 * points[2].x - points[0].x - points[1].x;
		result = fabs(result);
		if (result < s)
		{
			s = result;
			//pick_img = i;
			std::cout << s << std::endl;
			string Img_Name = "D:/Desktop/pachong/result/" + to_string(s) + ".jpg";
			imwrite(Img_Name, frame);
		}
		//imshow("img", imread(fn[pick_img]));
		//waitKey(1000);
	}

	return images;

}


