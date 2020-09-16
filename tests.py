from widget import Widget
import unittest

class TestWidget(unittest.TestCase):

    def test_show_widget(self):
        widget = Widget()
        self.assertTrue(widget.is_visible())

if __name__ == "__main__":
    unittest.main()
