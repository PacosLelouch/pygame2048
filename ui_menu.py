# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 350)
        MainWindow.setMinimumSize(QtCore.QSize(400, 350))
        MainWindow.setMaximumSize(QtCore.QSize(400, 350))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("2048.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    border-bottom: 1px solid;\n"
"    border-top: 0px solid;\n"
"    border-bottom-color: rgb(75, 175, 125);\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.0845771 rgba(32, 228, 128, 255), stop:0.60199 rgba(195, 251, 229, 200));\n"
"    \n"
"    font: 9pt \"华文新魏\";\n"
"}")
        self.centralWidget.setObjectName("centralWidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 400, 350))
        self.groupBox.setMinimumSize(QtCore.QSize(400, 350))
        self.groupBox.setMaximumSize(QtCore.QSize(400, 350))
        self.groupBox.setStyleSheet("QGroupBox{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.0199005 rgba(141, 246, 189, 150), stop:0.920398 rgba(69, 201, 245, 150));\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(100, 20, 201, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(110, 90, 181, 21))
        self.label_2.setStyleSheet("QLabel{\n"
"    \n"
"    font: 9pt \"华文彩云\";\n"
"}")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(110, 170, 181, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(0, 130, 400, 21))
        self.label_3.setStyleSheet("QLabel{\n"
"    \n"
"    font: 9pt \"华文彩云\";\n"
"}")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(150, 260, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(170, 220, 60, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.scoreboard = QtWidgets.QAction(MainWindow)
        self.scoreboard.setObjectName("scoreboard")
        '''
        self.help = QtWidgets.QAction(MainWindow)
        self.help.setObjectName("help")
        '''
        self.menu.addAction(self.scoreboard)
        #self.menu.addAction(self.help)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "2048"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">2<font color = \"blue\">0<font color = \"black\">4<font color = \"blue\">8</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">方向键控制方块移动方向</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">输入您的名字，选择地图尺寸，然后开始吧？</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "开始游戏"))
        self.comboBox.setItemText(0, _translate("MainWindow", "3"))
        self.comboBox.setItemText(1, _translate("MainWindow", "4"))
        self.comboBox.setItemText(2, _translate("MainWindow", "5"))
        self.comboBox.setItemText(3, _translate("MainWindow", "6"))
        self.comboBox.setItemText(4, _translate("MainWindow", "7"))
        self.comboBox.setItemText(5, _translate("MainWindow", "8"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.scoreboard.setText(_translate("MainWindow", "排行榜"))
        #self.help.setText(_translate("MainWindow", "帮助"))

