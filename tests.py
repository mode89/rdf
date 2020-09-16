from widget import Widget
import unittest

class TestWidget(unittest.TestCase):

    def test_widget_is_visible(self):
        widget = Widget()
        self.assertTrue(widget.is_visible())

    def test_initial_stage_is_red(self):
        widget = Widget()
        self.assertEqual(widget.get_stage(), Stage.RED)

if __name__ == "__main__":
    unittest.main()
