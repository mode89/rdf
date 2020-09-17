from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
import sys

class UI:

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = uic.loadUi("window.ui")
        assert isinstance(self.window, QMainWindow)
        self.window.setWindowFlag(QtCore.Qt.Tool)
        self.window.setAttribute(QtCore.Qt.WA_QuitOnClose)
        self.window.show()

    def run(self):
        self.app.exec_()

    def apply_stage(self, stage):
        self.set_stage_name(stage.name)
        self.set_stage_hint(stage.hint)
        self.set_stage_color(stage.color)

    def set_stage_name(self, name):
        raise NotImplementedError()

    def set_stage_hint(self, hint):
        raise NotImplementedError()

    def set_stage_color(self, color):
        raise NotImplementedError()
