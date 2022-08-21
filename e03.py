from manim import *

class BasicAnimations(Scene):
    def construct(self):
        polys = VGroup(
            *[RegularPolygon(5, radius=1) for j in range(5)]
        ).arrange(RIGHT)
        self.play(Create(polys))
        self.wait()