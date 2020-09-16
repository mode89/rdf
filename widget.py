class Widget:

    def __init__(self):
        self.stage = Stage.RED

    def is_visible(self):
        return True

    def get_stage(self):
        return self.stage

    def advance(self):
        if self.stage == Stage.RED:
            self.stage = Stage.GREEN

class Stage:

    RED = 1
    GREEN = 2
