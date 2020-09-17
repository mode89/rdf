from app import App
from app import GreenStage
from app import RedStage
from app import RefactorStage
import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
from ui import UI
import unittest
from unittest import mock

class TestApp(unittest.TestCase):

    def setUp(self):
        self.ui_class_patcher = mock.patch("app.UI", autospec=True)
        self.ui_class_patcher.start()
        self.app = App()

    def tearDown(self):
        self.ui_class_patcher.stop()

    def test_initial_stage_is_red(self):
        self.assertIsInstance(self.app.stage, RedStage)

    def test_advance_from_red_to_green(self):
        self.app.advance_stage()
        self.assertIsInstance(self.app.stage, GreenStage)

    def test_advance_from_green_to_refactor(self):
        self.app.advance_stage()
        self.app.advance_stage()
        self.assertIsInstance(self.app.stage, RefactorStage)

    def test_advance_from_refactor_to_red(self):
        self.app.advance_stage()
        self.app.advance_stage()
        self.app.advance_stage()
        self.assertIsInstance(self.app.stage, RedStage)

    def test_app_has_ui(self):
        self.assertIsInstance(self.app.ui, UI)

    def test_run_ui(self):
        self.app.run()
        self.app.ui.run.assert_called_once();

    def test_apply_stage_to_ui(self):
        self.app.apply_stage_class(RedStage)
        ui_apply_stage_first_argument = self.app.ui.apply_stage.call_args[0][0]
        self.assertIsInstance(ui_apply_stage_first_argument, RedStage)

    def test_set_advance_stage_callback(self):
        self.app.ui.set_advance_stage_callback.assert_called_once()

class TestUI(unittest.TestCase):

    def setUp(self):
        self.qapplication_patcher = mock.patch(
            "ui.QApplication", autospec=True)
        self.qapplication_patcher.start()
        self.uic_patcher = mock.patch("ui.uic", autospec=True)
        self.uic_mock = self.uic_patcher.start()
        self.uic_mock.loadUi.return_value = mock.create_autospec(
            PyQt5.QtWidgets.QMainWindow)
        self.ui = UI()

    def tearDown(self):
        self.uic_patcher.stop()
        self.qapplication_patcher.stop()

    def test_has_qapplication(self):
        self.assertIsInstance(self.ui.app, PyQt5.QtWidgets.QApplication)

    def test_has_window(self):
        self.assertIsInstance(self.ui.window, PyQt5.QtWidgets.QMainWindow)

    def test_run_app_exec(self):
        self.ui.run()
        self.ui.app.exec_.assert_called_once()

    def test_create_tool_window(self):
        self.ui.window.setWindowFlag.assert_called_with(Qt.Tool)
        self.ui.window.setAttribute.assert_called_with(Qt.WA_QuitOnClose)

    @mock.patch("ui.UI.set_stage_name")
    @mock.patch("ui.UI.set_stage_hint")
    @mock.patch("ui.UI.set_stage_color")
    def test_apply_red_stage(
            self,
            mock_set_stage_color,
            mock_set_stage_hint,
            mock_set_stage_name):
        stage = RedStage()
        self.ui.apply_stage(stage)
        self.ui.set_stage_name.assert_called_with(stage.name)
        self.ui.set_stage_hint.assert_called_with(stage.hint)
        self.ui.set_stage_color.assert_called_with(stage.color)

    def test_set_stage_name(self):
        self.ui.set_stage_name("Red")
        self.ui.stage_name_label.setText.assert_called_with("Red")

    def test_set_stage_hint(self):
        self.ui.set_stage_hint("Some hint")
        self.ui.stage_hint_label.setText.assert_called_with("Some hint")

    def test_advance_stage_keyboard_shortcut(self):
        callback = mock.Mock()
        self.ui.set_advance_stage_callback(callback)
        self.ui.on_advance_stage_keyboard_event()
        callback.assert_called_once()

    def test_set_key_press_event_handler(self):
        self.assertEqual(
            self.ui.window.keyPressEvent, self.ui.on_key_press_event)

    @mock.patch("ui.UI.on_advance_stage_keyboard_event")
    def test_fire_advance_stage_event_on_space_pressed(self, mock_callback):
        event = mock.create_autospec(QKeyEvent)
        event.key = mock.Mock(return_value=Qt.Key_Space)
        self.ui.on_key_press_event(event)
        self.ui.on_advance_stage_keyboard_event.assert_called_once()

if __name__ == "__main__":
    unittest.main()
