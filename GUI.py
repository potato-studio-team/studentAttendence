#################################################
# 这是一个由PotatoMan编写的应用于网课考勤的小程序
# 编写语言:Python 3
# 图形界面编写:PyQt5
# 编写时间:2020.3.12
# 详细说明请打开文件夹中的说明文件
# 本程序功能:统计网课考勤情况
#################################################

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import re
import datetime
import os

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
        
        self.pushButton.setText(_translate("MainWindow", "打开排除文件"))
        self.pushButton.clicked.connect(self.openTakeLeave)

        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">此处返回签到信息</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "  请输入班级学号最高值(数字) eg:最高为149==49，最高为246==46"))
        
        self.pushButton_2.setText(_translate("MainWindow", "打开输出文件"))
        self.pushButton_2.clicked.connect(self.openResult)

        self.pushButton_3.setText(_translate("MainWindow", "开始统计"))
        self.pushButton_3.clicked.connect(self.QUimain)

        self.pushButton_4.setText(_translate("MainWindow", "查看官网"))

        self.pushButton_5.setText(_translate("MainWindow", "文件修复"))
        self.pushButton_5.clicked.connect(self.fileMaker)

        self.pushButton_6.setText(_translate("MainWindow", "打开教程"))
        self.pushButton_6.clicked.connect(self.openTutoriar)

        self.menu.setTitle(_translate("MainWindow", "子雨网课考勤"))
        self.menu_2.setTitle(_translate("MainWindow", "开始考勤"))

# ======辅助功能槽函数定义====================================================

    def fileMaker(self):
        # self.QMessageBox.warning(self, "是否要修复文件", "文件修复后将替换之前的文件，你确定要继续？", QMessageBox.Yes | QMessageBox.No)
        # 目录判断创建
        dataR = ""
        if os.path.exists("StudentCode") == 0:
            os.mkdir("StudentCode")
        
        dataR = "创建目录成功\n"

        filehandle = open("StudentCode/result.txt",'w',encoding="utf-8")
        filehandle.write("###这里返回统计报告结果###")
        filehandle.close()
        dataR = dataR + "报告文件创建成功\n"

        filehandle = open("StudentCode/takeLeaveCode.txt",'w',encoding="utf-8")
        filehandle.close()
        dataR = dataR + "排除文件创建成功\n文件修复成功\n"

        self.textEdit_2.setText(dataR)

    # 打开报告文件
    def openResult(self):
        self.pushButton_2.setText("关闭文件")
        with open("StudentCode/result.txt", encoding="utf-8") as f:
            content = f.read()

        self.textEdit_2.setText(content)
        self.pushButton_2.clicked.connect(self.openResultC)

    def openResultC(self): 
        self.textEdit_2.setText("")
        self.pushButton_2.setText("打开输出文件")
        self.pushButton_2.clicked.connect(self.openResult)

    # 打开教程文件
    def openTutoriar(self):
        self.pushButton_6.setText("关闭文件")
        with open("about.txt", encoding="utf-8") as f:
            content = f.read()

        self.textEdit.setText(content)
        self.pushButton_6.clicked.connect(self.openTutoriarC)

    def openTutoriarC(self): 
        self.textEdit.setText("")
        self.pushButton_6.setText("打开教程")
        self.pushButton_6.clicked.connect(self.openTutoriar)

    # 打开排除文件
    def openTakeLeave(self):
        # os.system("cd StudentCode")
        place = os.getcwd()
        place = str(place)
        place = place + "/takeLeaveCode.txt"
        os.startfile(place)
        self.textEdit_2.setText("已打开文件")

# ======主程序槽函数定义======================================================

    def QUimain(self):
        # 获取输入框内容
        grade = int(self.lineEdit.text())
        aims = int(self.lineEdit_2.text())
        codeData = str(self.textEdit.toPlainText())

        # 正则分析
        lsCode = re.findall(r"[0-9]{3,3}?", codeData)
        print(type(lsCode))
        
# 考勤分析-------------------------------------------------------------------

        lsA = aims + 1
        lsAD = ["#缺席#"]*lsA
        lsAD[0] = "序号####学号"

        print(lsCode)
        print(type(lsCode))
        
        print(grade)

        for i in lsCode:
            i = int(i)
            lsi = i - grade * 100
            lsiNot = str(lsi)
            n = "   "
            ii = str(i)
            lsAD[lsi] = lsiNot + n + ii

# 请假处理--------------------------------------------------------------------

        with open("StudentCode/takeLeaveCode.txt", encoding="utf-8") as f:
            content = f.readlines()

        takeLeave = content

        grade = int(grade)

        for i in takeLeave:
            i.strip("\n")
            i = int(i)
            i = i - grade * 100
            lsAD[i] = "#请假#" 

# 缺席处理---------------------------------------------------------------------
        
        a = 0
        aa = 0
        lsAbD = ""
        grade = str(grade)

        while(a <= aims):
            if lsAD[a] == "#缺席#":
                aaa = a
                aaa = str(aaa)
                lsAbD = lsAbD + aaa + ","
                aa = aa + 1
            a = a + 1

# 输出处理---------------------------------------------------------------------

        lsADD = ""
        for i in lsAD:
            lsADD = lsADD + "\n" + i

        today = datetime.date.today()
        today = str(today)

        result = "\n\n子雨网课考勤报告\n" + "详细请查看StudentCode/result.txt" + "日期\n" + today + "\n\n考勤统计\n" + lsADD + "\n\n缺席统计\n" + lsAbD

        # 写文件
        filehandle = open("StudentCode/result.txt",'a', encoding="utf-8")
        filehandle.write(result)
        filehandle.close()

        self.textEdit_2.setText(result)


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