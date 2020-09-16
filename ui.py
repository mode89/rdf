from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
import sys

class UI:

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = uic.loadUi("window.ui")
        assert isinstance(self.window, QMainWindow)
        self.window.show()

    def run(self):
        self.app.exec_()
