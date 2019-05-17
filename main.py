import sys
from menu import Menu
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu_window = Menu()
    menu_window.show()
    sys.exit(app.exec_())
