# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scoreboard2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 400)
        Dialog.setMinimumSize(QtCore.QSize(300, 400))
        Dialog.setMaximumSize(QtCore.QSize(300, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("2048.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("QPushButton{border-radius: 5px;border-bottom: 1px solid;border-top: 0px solid;border-bottom-color: rgb(75, 175, 125);background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.0845771 rgba(32, 228, 128, 255), stop:0.60199 rgba(195, 251, 229, 200));}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("QLabel{\n"
"    font: 9pt \"华文彩云\";\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Yes = QtWidgets.QPushButton(Dialog)
        self.Yes.setMinimumSize(QtCore.QSize(0, 30))
        self.Yes.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Yes.setObjectName("Yes")
        self.horizontalLayout.addWidget(self.Yes)
        self.No = QtWidgets.QPushButton(Dialog)
        self.No.setMinimumSize(QtCore.QSize(0, 30))
        self.No.setMaximumSize(QtCore.QSize(16777215, 30))
        self.No.setObjectName("No")
        self.horizontalLayout.addWidget(self.No)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "排行榜"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "昵称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "分数"))
        self.label.setText(_translate("Dialog", "您的昵称：\n"
"最新的分数：\n"
"要保存吗？"))
        self.Yes.setText(_translate("Dialog", "保存"))
        self.No.setText(_translate("Dialog", "不保存"))

