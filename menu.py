from ui_menu import Ui_MainWindow
from scoreboard import Scoreboard
from game import Game
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dialog = None
        self.game = None
        self.ui.scoreboard.triggered.connect(self.scoreBoard)
        #self.ui.help.triggered.connect(self.help)
        self.ui.pushButton.pressed.connect(self.buttonPress)
        self.ui.pushButton.released.connect(self.buttonRelease)
        self.ui.pushButton.clicked.connect(self.start)

    def scoreBoard(self):
        try:
            if self.dialog:
                self.dialog.close()
            #下一行测试用的
            #self.dialog = Scoreboard(use_zip=True, write=True, name0='江沢', score0=817)
            self.dialog = Scoreboard(use_zip=True, size_str=self.ui.comboBox.currentText())
            self.dialog.show()
        except Exception as e:
            print("Scoreboard error.")
            print(str(e))

    def help(self):
        print("还有什么功能需要加？")#TODO
        try:
            pass
        except Exception as e:
            print(str(e))

    def start(self):
        if self.ui.lineEdit.text() == '':
            return
        try:
            if self.game:
                del(self.game)
            print(self.ui.comboBox.currentText())
            self.game = Game(self.ui.lineEdit.text().replace(' ', '_'), 400, 600, int(self.ui.comboBox.currentText()))
            self.game.run()
        except Exception as e:
            print("Game error.")
            print(str(e))

    def buttonPress(self):
        self.ui.pushButton.setStyleSheet("QPushButton{border-radius: 5px;border-bottom: 0px solid;border-top: 1px solid;border-top-color: rgb(75, 175, 125);background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.0845771 rgba(13, 204, 88, 255), stop:0.60199 rgba(153, 224, 198, 200));}")
		
    def buttonRelease(self):
        self.ui.pushButton.setStyleSheet("QPushButton{border-radius: 5px;border-bottom: 1px solid;border-top: 0px solid;border-bottom-color: rgb(75, 175, 125);background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.0845771 rgba(32, 228, 128, 255), stop:0.60199 rgba(195, 251, 229, 200));}")
        
