from manim import *

class FirstExample(Scene):
    def construct(self):
        blue_dot = Dot(color=BLUE)
        dot_label = Text("Hello dot!").next_to(blue_dot, UP)
        dot_label.add_updater(
            lambda mobject: mobject.next_to(blue_dot, UP)
        )
        self.add(blue_dot, dot_label)
        self.play(blue_dot.animate.shift(RIGHT))
        self.play(blue_dot.animate.scale(3))
        self.play(blue_dot.animate.center())