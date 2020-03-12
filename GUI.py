# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import re
import datetime

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(997, 553)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")

        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_2.addWidget(self.textEdit_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_3.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_5.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_5.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_5.addWidget(self.pushButton_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 997, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">请输入评论（包含签到）内容</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "  请输入班级(数字)，eg:一班==1，二班==2"))
        self.pushButton.setText(_translate("MainWindow", "打开输入文件"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">此处返回签到信息</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "  请输入班级学号最高值(数字) eg:最高为149==49，最高为246==46"))
        self.pushButton_2.setText(_translate("MainWindow", "打开输出文件"))

        self.pushButton_3.setText(_translate("MainWindow", "开始统计"))
        self.pushButton_3.clicked.connect(self.QUimain)

        self.pushButton_4.setText(_translate("MainWindow", "文件修复"))
        self.pushButton_5.setText(_translate("MainWindow", "打开教程"))
        self.pushButton_6.setText(_translate("MainWindow", "打开排除文件"))
        self.menu.setTitle(_translate("MainWindow", "子雨网课考勤"))
        self.menu_2.setTitle(_translate("MainWindow", "开始考勤"))


    # 主程序开始

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
        lis = ["#缺席#"] * aims
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
        while (i <= aims):
            if list[i] == "#缺席#":
                iii = i
                iii = str(iii)
                lsa = lsa + iii + ","
                ii = ii + 1
            i = i + 1

        return lsa

    def takeLeave(takeLeave, attendance, grade):
        grade = int(grade)
        for i in takeLeave:
            i.strip("\n")
            i = int(i)
            i = i - grade * 100
            attendance[i] = "#请假#"

            # attendance.remove('')
        return attendance

    def writeFile(place, data01, data02):
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

    def QUimain(self):
        grade = int(input("\n# 请输入班级(数字)\n# eg:一班==1，二班==2\n>>>"))
        aims = int(input("\n# 请输入班级学号最高值(数字)\n# eg:最高为149==49，最高为246==46\n>>>"))
        print("\n--分析文件--")
        codeData = readFile("StudentCode/inputStudentCode.txt")
        resultCheck = studentCodeCheck(codeData, r'[0-9]{3,3}?')

        result = studentCodeStatistics(resultCheck, aims, grade)

        takeLeaveData = readFileLine("StudentCode/takeLeaveCode.txt")

        result = takeLeave(takeLeaveData, result, grade)

        absent = absentSearch(result, aims, grade)
        print(absent)
        writeFile("StudentCode/result.txt", result, absent)
        print("\n###已生成报告，请在StudentCode/result.txt查看")
        input("\n回车退出软件，谢谢使用")

def main():
    if __name__ == '__main__':
        # application 对象
        app = QApplication(sys.argv)
        # QMainWindow对象
        mainwindow = QMainWindow()
        # 这是qt designer实现的Ui_MainWindow类
        ui_components = Ui_MainWindow()
        # 调用setupUi()方法，注册到QMainWindwo对象
        ui_components.setupUi(mainwindow)
        # 显示
        mainwindow.show()
        sys.exit(app.exec_())
main()