from re import L, S
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

        c2 = Circle(radius=0.5, color=RED, fill_opacity=0.5)
        c3 = c2.copy().set_color(ORANGE)
        c4 = c2.copy().set_color(YELLOW)
        c2.align_to(s, UP)
        c3.align_to(s, RIGHT)
        c4.align_to(s, UP + RIGHT)
        self.add(c2, c3, c4)

class CriticalPoints(Scene):
    def construct(self):
        c = Circle(color=GREEN, fill_opacity=0.5)
        self.add(c)

        for d in [(0,0,0), UP, DOWN, LEFT, RIGHT, UL, UR, DL, DR]:
            self.add(Cross(scale_factor=0.2).move_to(c.get_critical_point(d)))

        s = Square(color=RED, fill_opacity=0.5)
        s.move_to([1,0,0], aligned_edge=LEFT)
        self.add(s)