#################################################
# 这是一个由PotatoMan编写的应用于网课考勤的小程序
# 编写语言:Python 3
# 编写时间:2020.3.21
# 详细说明请打开文件夹中的说明文件
# 本程序功能:统计网课考勤情况
#################################################

import re
import datetime


def readFile(place):
    with open(place, encoding="utf-8") as f:
        content = f.read()
    return content
    
# 读取文件并返回列表格式
def readFileLine(place):
    with open(place, encoding="utf-8") as f:
        content = f.readlines()
    return content

def studentCodeCheck(data, check):
    check = str(check)
    ls = re.findall(check, data)
    return ls

def studentCodeStatistics(data, aims, grade):
    aims = aims + 1
    lis = ["#缺席#"]*aims
    lis[0] = "序号####学号"

    for i in data:
        i = int(i)
        lsi = i - grade * 100
        lsiNot = str(lsi)
        n = "   "
        ii = str(i)
        lis[lsi] = lsiNot + n + ii

    return lis

def absentSearch(list, aims, grade):
    i = 0
    ii = 0
    lsa = ""
    grade = str(grade)
    while(i <= aims):
        if list[i] == "#缺席#":
            iii = i
            iii = str(iii)
            lsa = lsa + iii + ","
            ii = ii + 1
        i = i + 1

    return lsa

def takeLeave(takeLeave,attendance,grade):
    grade = int(grade)
    for i in takeLeave:
        i.strip("\n")
        i = int(i)
        i = i - grade * 100
        attendance[i] = "#请假#" 

    # attendance.remove('')
    return attendance

def writeFile(place,data01,data02):
    filehandle = open(place, 'w', encoding="utf-8")
    filehandle.write("这是本次考勤的报告")

    filehandle.write("\n生成日期\n##")
    today = datetime.date.today()
    today = str(today)
    filehandle.write(today)

    filehandle.write("##\n\n签到报告\n")
    for i in data01:
        iWr = str(i)
        iWr = iWr + "\n"
        filehandle.write(iWr)

    filehandle.write("\n\n缺席报告\n")
    for i02 in data02:
        iWr2 = str(i02)
        iWr2 = iWr2 + "  "
        filehandle.write(iWr2)
    filehandle.close()

def main():
    print("###########欢迎使用网课考勤统计小程序############\n# 这是一个由PotatoMan编写的应用于网课考勤的小程序\n# 编写语言:Python 3\n# 编写时间:2020.3.21\n# 详细说明请打开文件夹中的说明文件\n# 本程序功能:统计网课考勤情况\n#################################################")

    grade = int(input("\n# 请输入班级(数字)\n# eg:一班==1，二班==2\n>>>"))
    aims = int(input("\n# 请输入班级学号最高值(数字)\n# eg:最高为149==49，最高为246==46\n>>>"))

    print("\n###请确认StudentCode内文件完好，信息已复制###\n###如StudentCode内文件残缺或目录残缺，请运行:修复文件###\n###程序执行将会替换原有报告文件###")
    check = input("\n#确认完成，请输入Y开始执行，N退出\n>>>")

    if check == "y" or check == "Y":
        print("\n--分析文件--")
        codeData = readFile("StudentCode/inputStudentCode.txt")
        resultCheck = studentCodeCheck(codeData, r'[0-9]{3,3}?')
        print("\n--分析成功--")
        
        print("\n--生成签到--")
        result = studentCodeStatistics(resultCheck, aims, grade)
        print("\n--生成成功--")

        print("\n--处理请假--")
        takeLeaveData = readFileLine("StudentCode/takeLeaveCode.txt")
        result = takeLeave(takeLeaveData, result, grade)
        print("\n--处理成功--")
        
        print("\n--处理缺席--")
        absent = absentSearch(result, aims, grade)
        print("\n--处理成功--")
        
        print("\n###已生成缺席列表如下###")
        print(absent)
        
        writeFile("StudentCode/result.txt", result, absent)
        print("\n###已生成报告，请在StudentCode/result.txt查看")
        input("\n回车退出软件，谢谢使用")


    elif check == "n" or check == "N":
        print("退出")

main()
