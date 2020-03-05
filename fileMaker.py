#################################################
# 这是一个由PotatoMan编写的应用于网课考勤的小程序
# 编写语言:Python 3
# 编写时间:2020.3.21
# 详细说明请打开data文件夹中的说明文件
# 本程序功能:如果误删，在此次创建所需文件
#################################################

import os
def writeFile(place,data):
    filehandle = open(place,'w',encoding="utf-8")
    filehandle.write(data,)
    filehandle.close()

def writePlace(place):
    if os.path.exists(place) == 0:
        os.mkdir(place)

def main():
    writePlace("StudentCode")
    writeFile("StudentCode/inputStudentCode.txt", "###在这里输入你复制的信息###")
    writeFile("StudentCode/result.txt", "###这里返回统计报告结果###")
    writeFile("StudentCode/takeLeaveCode.txt","")

main()
