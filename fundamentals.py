from manim import *

SECONDS = 10

class AddWaitRemove(Scene):
    def construct(self):
        square = Square()
        self.add(square)
        self.wait()
        self.remove(square)
        self.wait()

with tempconfig({"quality": "high_quality", "preview": True}):
    scene = AddWaitRemove()
    scene.render()