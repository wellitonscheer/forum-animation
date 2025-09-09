from manim import *

class SquareToCircle(Scene):
  def construct(self):
    circle = Circle()
    circle.set_fill(PINK, opacity=0.5)

    square = Square()
    square.rotate(PI / 4)

    self.play(Create(square))
    self.play(Transform(square, circle))
    self.play(FadeOut(square))


class SquareAndCircle(Scene):
  def construct(self):
    circle = Circle()
    circle.set_fill(PINK, opacity=0.5)

    square = Square()
    square.set_fill(BLUE, opacity=0.5)

    square.next_to(circle, RIGHT, buff=0.1)
    self.play(Create(square), Create(circle))

    