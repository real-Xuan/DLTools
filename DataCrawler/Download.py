#_*_coding:utf-8_*_
import os
from multiprocessing import Pool

import requests


class DownloadFile():
    '''根据提供的Url下载文件'''

    def __init__(self,download_file_path,save_path = 'D:\ossdownloads'):
        self.download_file = download_file_path
        self.save_path = save_path

    def get_content(self):
        '''获取所有文件的链接和对应的文件格式'''
        urls = []
        with open(self.download_file,'r') as f: 
            contents = f.readlines()
            for content in contents:
                url = content.strip()
                f_name = url.split('/')[-1]
                urls.append((url,f_name))
        #print(urls)
        return urls

    def save(self,urls):
        '''下载文件并保存到指定地址'''
        url = urls[0]
        f_name = urls[1]
        try:
            file = requests.get(url)
            file.raise_for_status()
        except requests.RequestException as e:
            print(e)
        else:
            with open(self.save_path + '\\' + f_name, 'wb') as f:
                # print(self.save_path+f_name)
                f.write(file.content)
        for root, dirs, files in os.walk(self.save_path):
            print('已完成 %d 个下载'%(len(files)))

    def download(self):
        if __name__ == '__main__':
            urls = self.get_content()
            print('共有 %d 个文件等待下载'%(len(urls)))
            p=Pool(8)
            p.map(self.save, urls)
            p.close()
            p.join()
            for root, dirs, files in os.walk(self.save_path):
                print('下载结束，共下载 %d 个文件'%(len(files)))



#下载链接文件路径
down_path = r'D:/Desktop/ExcelToTxt/活体检测采集方案0514部分数据返回/活体检测采集方案0514部分数据返回/result.txt'
#下载文件的存储路径
save_path = r'D:/Desktop/ExcelToTxt/'

a = DownloadFile(down_path, save_path=save_path)
a.download()



