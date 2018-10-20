import os
 
file = open("D:/Working_Area/Test_data/IDIAP_RepalyAttack_avi/TXT/attack-grandtest-hand-test.txt")
lines = file.readlines()
for line in lines:
    b = line.split('.')
    b.pop()
    b.append('.avi')
    str = ''
    c = str.join(b)
    print(c)
    
# 以写的方式打开文件，如果文件不存在，就会自动创建
    file_write = open("list.txt", 'a')
    file_write.writelines(c)
    file_write.write('\n')
    file_write.close()

file.close()