from manim import *
from colour import Color

class BasicAnimations(Scene):
    def construct(self):
        polys = VGroup(
            *[RegularPolygon(5, radius=1, fill_opacity=0.5,
            color=Color(hue=j/5,saturation=1,luminance=0.5)) for j in range(5)]
        ).arrange(RIGHT)
        self.play(DrawBorderThenFill(polys, run_time=2))
        self.play(
            Rotate(polys[0], PI, rate_func=lambda t: t),
            Rotate(polys[1], PI, rate_func=smooth),
            Rotate(polys[2], PI, rate_func=lambda t: np.sin(PI*t)),
            Rotate(polys[3], PI, rate_func=there_and_back),
            Rotate(polys[4], PI, rate_func=lambda t: 1-abs(1-2*t)),
            run_time=2
        )
        self.wait()

class ConflictingAnimations(Scene):
    def construct(self):
        s = Square()
        self.play(Rotate(s,PI),Rotate(s,-PI), run_time=3)

class LaggingGroup(Scene):
    def construct(self):
        squares = VGroup(*[Square(color=Color(hue=j/20,saturation=1,luminance=0.5),
        fill_opacity=0.5) for j in range(20)]).arrange_in_grid(4,5).scale(0.75)
        self.play(AnimationGroup(*[FadeIn(s) for s in squares], lag_ratio=0.15))

class AnimateSyntax(Scene):
    def construct(self):
        s = Square(color=GREEN, fill_opacity=0.5)
        c = Circle(color=RED, fill_opacity=0.5)
        self.add(s,c)

        self.play(s.animate.shift(UP), c.animate.shift(DOWN))
