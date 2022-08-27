from manim import *

class SuccessionExample(Scene):
    def construct(self):
        number_line=NumberLine(x_range=(-2,2))
        triangle=RegularPolygon(3,start_angle=-PI/2)\
                   .scale(0.2)\
                   .next_to(number_line.get_left(),UP,buff=SMALL_BUFF)
        text_1=Text("1")\
               .next_to(number_line.get_tick(-1),DOWN)
        text_2=Text("2")\
               .next_to(number_line.get_tick(0),DOWN)
        text_3=Text("3")\
               .next_to(number_line.get_tick(1),DOWN)
        text_4=Text("4")\
               .next_to(number_line.get_tick(2),DOWN)

        self.add(number_line)
        #self.play(Create(triangle))

        self.play(
                    #The move of the triangle starts
                    #ApplyMethod(triangle.shift,RIGHT*4,rate_func=linear,run_time=4),

                    AnimationGroup(
                        Animation(Mobject(),run_time=1),#<- one second pause
                        Write(text_1),lag_ratio=1       #<- then start Write animation
                    ),
                    AnimationGroup(
                        Animation(Mobject(),run_time=2),#<- two seconds pause
                        Write(text_2),lag_ratio=1       #<- then start Write animation
                    ),
                    AnimationGroup(
                        Animation(Mobject(),run_time=3),#<- three seconds pause
                        Write(text_3),lag_ratio=1       #<- then start Write animation
                    ),
                    AnimationGroup(
                        Animation(Mobject(),run_time=4),#<- four seconds pause
                        Write(text_4),lag_ratio=1       #<- then start Write animation
                    )
            )

with tempconfig({"quality": "high_quality", "preview": True}):
    scene = SuccessionExample()
    scene.render()