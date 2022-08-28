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

class AllUpdaterTypes(Scene):
    def construct(self):
        red_dot = Dot(color=RED).shift(LEFT)
        pointer = Arrow(ORIGIN, RIGHT).next_to(red_dot, LEFT)
        pointer.add_updater(
            lambda mobject: mobject.next_to(red_dot, LEFT)
        )

        def shifter(mob, dt):
            mob.shift(2*dt*RIGHT)
        red_dot.add_updater(shifter)

        def scene_scaler(dt):
            for mob in self.mobjects:
                mob.set(width=2/(1 + np.linalg.norm(mob.get_center())))
        self.add_updater(scene_scaler)

        self.add(red_dot, pointer)
        self.update_self(0)
        self.wait(5)