from widget import Widget
import unittest

class TestWidget(unittest.TestCase):

    def test_widget_is_visible(self):
        widget = Widget()
        self.assertTrue(widget.is_visible())

if __name__ == "__main__":
    unittest.main()
