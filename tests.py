from widget import Stage, Widget
import unittest

class TestWidget(unittest.TestCase):

    def test_widget_is_visible(self):
        widget = Widget()
        self.assertTrue(widget.is_visible())

    def test_initial_stage_is_red(self):
        widget = Widget()
        self.assertEqual(widget.stage, Stage.RED)

    def test_advance_from_red_to_green(self):
        widget = Widget()
        widget.advance_stage()
        self.assertEqual(widget.stage, Stage.GREEN)

if __name__ == "__main__":
    unittest.main()
