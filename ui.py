import debug
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
import sys

class UI:

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = uic.loadUi("window.ui")
        assert isinstance(self.window, QMainWindow)
        self.window.setWindowFlag(Qt.Tool)
        self.window.setAttribute(Qt.WA_QuitOnClose)
        self.window.show()
        self.stage_name_label = self.window.findChild(QLabel, "stage_name")
        assert self.stage_name_label
        self.stage_hint_label = self.window.findChild(QLabel, "stage_hint")
        assert self.stage_hint_label
        self.window.keyPressEvent = self.on_key_press_event

    def run(self):
        self.app.exec_()

    def apply_stage(self, stage):
        self.set_stage_name(stage.name)
        self.set_stage_hint(stage.hint)
        self.set_stage_color(stage.color)

    def set_stage_name(self, name):
        self.stage_name_label.setText(name)

    def set_stage_hint(self, hint):
        self.stage_hint_label.setText(hint)

    def set_stage_color(self, color):
        self.window.setStyleSheet("background-color: {}".format(color))

    def set_advance_stage_callback(self, callback):
        self.advance_stage_callback = callback

    def on_advance_stage_keyboard_event(self):
        self.advance_stage_callback()

    def on_key_press_event(self, event):
        if event.key() == Qt.Key_Space:
            self.on_advance_stage_keyboard_event()
