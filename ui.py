from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import sys

class UI:

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = uic.loadUi("window.ui")
        self.window.show()

    def run(self):
        self.app.exec_()
