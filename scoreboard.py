# -*- coding: utf-8 -*-

from ui_scoreboard1 import Ui_Dialog as Ui_Dialog1
from ui_scoreboard2 import Ui_Dialog as Ui_Dialog2
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
import gzip # 加密压缩用

class Scoreboard(QDialog):
    def __init__(self, size_str='4', use_zip=True, write=False, name0='', score0=-1):
        super().__init__()
        if write:
            self.ui = Ui_Dialog2()
            self.ui.setupUi(self)
            self.ui.Yes.pressed.connect(self.buttonPressYes)
            self.ui.Yes.released.connect(self.buttonReleaseYes)
            self.ui.No.pressed.connect(self.buttonPressNo)
            self.ui.No.released.connect(self.buttonReleaseNo)
            self.ui.Yes.clicked.connect(self.save)
            self.ui.No.clicked.connect(self.close)
            self.saved = False
            self.name0 = name0
            self.score0 = score0
            self.ui.label.setText('您的昵称：' + name0 + '\n最新的分数：' + str(score0) + '\n要保存吗？')
        else:
            self.ui = Ui_Dialog1()
            self.ui.setupUi(self)
        self.write = write
        self.fname = 'scoreboard' + size_str + '.data'
        self.setWindowTitle("排行榜(" + size_str + "x" + size_str + ")")
        self.scores = []
        self.use_zip = use_zip
        try:
            self.readFile()
        except Exception as e:
            print('Scoreboard error.')
            print(str(e))

    def readFile(self):
        with open(self.fname, 'ab') as f:
            f.close()
        with Scoreboard.open(self.fname, 'rb', self.use_zip) as f:
            s0 = str(f.read(), encoding='utf-8')
            #'''test
            print(s0)
            #'''
            s = s0.split()
            s1 = [s[i] for i in range(len(s)) if i & 1 == 0]
            s2 = [int(s[i]) for i in range(len(s)) if i & 1]
            row, rank, currentScore = 1, 1, 2147483647
            self.scores = sorted(zip(s1, s2), key=lambda a:a[1], reverse=True)
            self.ui.tableWidget.setRowCount(len(self.scores))
            for name, score in self.scores:
                if currentScore > score:
                    rank = row
                    currentScore = score
                self.ui.tableWidget.setVerticalHeaderItem(row - 1, QTableWidgetItem(str(rank)))
                self.ui.tableWidget.setItem(row - 1, 0, QTableWidgetItem(name))
                self.ui.tableWidget.setItem(row - 1, 1, QTableWidgetItem(str(score)))
                row += 1
        self.ui.tableWidget.setColumnWidth(0, 120)
        self.ui.tableWidget.setColumnWidth(1, 80)
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def save(self):
        if not self.write:
            return
        if self.saved:
            self.ui.label.setText('您已经保存过了……')
            return
        try:
            if self.use_zip:
                self.save_gzip()
            else:
                self.save_append()
            self.ui.label.setText('已保存')
            self.saved = True
            self.ui.No.setEnabled(False)
            #self.buttonDisable(self.ui.No)
        except Exception as e:
            print('Save error')
            print(str(e))

    def open(file, mode, use_zip):
        if use_zip:
            return gzip.open(file, mode)
        else:
            return open(file, mode)

    def save_append(self):
        row, rank, currentScore = 1, 1, 2147483647
        self.scores.append((self.name0, self.score0))
        self.ui.tableWidget.setRowCount(len(self.scores))
        self.scores.sort(key=lambda a:a[1], reverse=True)
        for name, score in self.scores:
            if currentScore > score:
                rank = row
                currentScore = score
            self.ui.tableWidget.setVerticalHeaderItem(row - 1, QTableWidgetItem(str(rank)))
            self.ui.tableWidget.setItem(row - 1, 0, QTableWidgetItem(name))
            self.ui.tableWidget.setItem(row - 1, 1, QTableWidgetItem(str(score)))
            row += 1
        
        with open(self.fname, 'ab') as f:
            if self.use_zip:
                f.write(gzip.compress(bytes('%s %d\n'%(self.name0, self.score0), encoding='utf-8')))
            else:
                f.write(bytes('%s %d\n'%(self.name0, self.score0), encoding='utf-8'))

    def save_gzip(self):
        new_str = ''
        row, rank, currentScore = 1, 1, 2147483647
        self.scores.append((self.name0, self.score0))
        self.ui.tableWidget.setRowCount(len(self.scores))
        self.scores.sort(key=lambda a:a[1], reverse=True)
        for name, score in self.scores:
            if currentScore > score:
                rank = row
                currentScore = score
            self.ui.tableWidget.setVerticalHeaderItem(row - 1, QTableWidgetItem(str(rank)))
            self.ui.tableWidget.setItem(row - 1, 0, QTableWidgetItem(name))
            self.ui.tableWidget.setItem(row - 1, 1, QTableWidgetItem(str(score)))
            row += 1
            new_str += '%s %d\n'%(name, score)
        
        with open(self.fname, 'wb') as f:
            f.write(gzip.compress(bytes(new_str, encoding='utf-8')))

    def buttonPressYes(self):
        self.ui.Yes.setStyleSheet("QPushButton{border-radius: 5px;border-bottom: 0px solid;border-top: 1px solid;border-top-color: rgb(75, 175, 125);background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.0845771 rgba(13, 204, 88, 255), stop:0.60199 rgba(153, 224, 198, 200));}")
		
    def buttonReleaseYes(self):
        self.ui.Yes.setStyleSheet("QPushButton{border-radius: 5px;border-bottom: 1px solid;border-top: 0px solid;border-bottom-color: rgb(75, 175, 125);background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.0845771 rgba(32, 228, 128, 255), stop:0.60199 rgba(195, 251, 229, 200));}")

    def buttonPressNo(self):
        self.ui.No.setStyleSheet("QPushButton{border-radius: 5px;border-bottom: 0px solid;border-top: 1px solid;border-top-color: rgb(75, 175, 125);background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.0845771 rgba(13, 204, 88, 255), stop:0.60199 rgba(153, 224, 198, 200));}")
		
    def buttonReleaseNo(self):
        self.ui.No.setStyleSheet("QPushButton{border-radius: 5px;border-bottom: 1px solid;border-top: 0px solid;border-bottom-color: rgb(75, 175, 125);background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.0845771 rgba(32, 228, 128, 255), stop:0.60199 rgba(195, 251, 229, 200));}")
     
