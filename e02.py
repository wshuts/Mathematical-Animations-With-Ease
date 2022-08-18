from manim import *

class Positioning(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)

        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN)
        green_dot.next_to(red_dot, RIGHT + UP)
        self.add(red_dot, green_dot)

        s = Square(color=ORANGE)
        s.shift(4*RIGHT + 2*UP)
        self.add(s)

        c = Circle(color=PURPLE)
        c.move_to([-3,-2,0])
        self.add(c)

