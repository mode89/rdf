from enum import Enum

Stage = Enum("Stage", [ "RED", "GREEN", "REFACTOR" ])

class Widget:

    def __init__(self):
        self.stage = Stage.RED

    def is_visible(self):
        return True

    def advance_stage(self):
        if self.stage == Stage.RED:
            self.stage = Stage.GREEN
        elif self.stage == Stage.GREEN:
            self.stage = Stage.REFACTOR
