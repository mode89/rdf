from enum import Enum

Stage = Enum("Stage", [ "RED", "GREEN", "REFACTOR" ])

class App:

    def __init__(self):
        self.stage = Stage.RED

    def run(self):
        pass

    def advance_stage(self):
        if self.stage == Stage.RED:
            self.stage = Stage.GREEN
        elif self.stage == Stage.GREEN:
            self.stage = Stage.REFACTOR
        elif self.stage == Stage.REFACTOR:
            self.stage = Stage.RED

if __name__ == "__main__":
    app = App()
    app.run()
