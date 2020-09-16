from app import Stage, App
from ui import UI
import unittest
from unittest import mock

class TestApp(unittest.TestCase):

    def setUp(self):
        self.patch_ui_class = mock.patch("app.UI", autospec=True)
        self.patch_ui_class.start()
        self.app = App()

    def tearDown(self):
        self.patch_ui_class.stop()

    def test_initial_stage_is_red(self):
        self.assertEqual(self.app.stage, Stage.RED)

    def test_advance_from_red_to_green(self):
        self.app.advance_stage()
        self.assertEqual(self.app.stage, Stage.GREEN)

    def test_advance_from_green_to_refactor(self):
        self.app.advance_stage()
        self.app.advance_stage()
        self.assertEqual(self.app.stage, Stage.REFACTOR)

    def test_advance_from_refactor_to_red(self):
        self.app.advance_stage()
        self.app.advance_stage()
        self.app.advance_stage()
        self.assertEqual(self.app.stage, Stage.RED)

    def test_app_has_ui(self):
        self.assertIsInstance(self.app.ui, UI)

if __name__ == "__main__":
    unittest.main()
