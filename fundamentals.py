from manim import *

SECONDS = 10

class AddWaitRemove(Scene):
    def construct(self):
        
        for _ in range(SECONDS):
            square = Square()
            self.AddWait(square)
            self.ShiftWait(square, 1)
            self.RemoveWait(square)

    def ShiftWait(self, square, shift):
        square.shift(RIGHT*shift)
        self.wait()

    def RemoveWait(self, square):
        self.remove(square)
        self.wait()

    def AddWait(self, square):
        self.add(square)
        self.wait()
        return square

with tempconfig({"quality": "high_quality", "preview": True}):
    scene = AddWaitRemove()
    scene.render()