import debug
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
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
        self.stage_name_label = self.window.findChild(QLabel, "stage_name")
        assert self.stage_name_label

    def run(self):
        self.app.exec_()

    def apply_stage(self, stage):
        self.set_stage_name(stage.name)
        self.set_stage_hint(stage.hint)
        self.set_stage_color(stage.color)

    def set_stage_name(self, name):
        self.stage_name_label.setText(name)

    def set_stage_hint(self, hint):
        debug.not_implemented()

    def set_stage_color(self, color):
        debug.not_implemented()
