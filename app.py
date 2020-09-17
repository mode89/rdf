from ui import UI

class App:

    def __init__(self):
        self.ui = UI()
        self.stage = RedStage

    def run(self):
        self.ui.run()

    def advance_stage(self):
        if self.stage == RedStage:
            self.stage = GreenStage
        elif self.stage == GreenStage:
            self.stage = RefactorStage
        elif self.stage == RefactorStage:
            self.stage = RedStage

class RedStage:

    def __init__(self):
        self.name = "RED"
        self.hint = "Write a test, watch it fail"
        self.color = "red"

class GreenStage:

    pass

class RefactorStage:

    pass

if __name__ == "__main__":
    app = App()
    app.run()
