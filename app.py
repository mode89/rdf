from enum import Enum
from ui import UI

Stage = Enum("Stage", [ "RED", "GREEN", "REFACTOR" ])

class App:

    def __init__(self):
        self.ui = UI()
        self.stage = Stage.RED

    def run(self):
        self.ui.run()

    def advance_stage(self):
        if self.stage == Stage.RED:
            self.stage = Stage.GREEN
        elif self.stage == Stage.GREEN:
            self.stage = Stage.REFACTOR
        elif self.stage == Stage.REFACTOR:
            self.stage = Stage.RED

class RedStage:

    def __init__(self):
        self.name = "RED"
        self.hint = "Write a test, watch it fail"
        self.color = "red"

if __name__ == "__main__":
    app = App()
    app.run()
