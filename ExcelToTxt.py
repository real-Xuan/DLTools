import numpy as np
import xlrd

data= xlrd.open_workbook('D:/Desktop/ExcelToTxt/活体检测采集方案0514部分数据返回/6.xlsx')
sh=data.sheet_by_name("sheet1")
print(sh.nrows)
print(sh.ncols)
n=0
i=0
file=open("ng.txt","a")
for n in range(sh.nrows):
    text = sh.cell_value(n,0)
    file.write(text) 
    file.write('\n') 
    
print("All Set")