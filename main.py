from manim import *

class CreateCirle(Scene):
  def construct(self):
    circle = Circle()
    circle.set_fill(PINK, opacity=0.5)
    self.play(Create(circle))
    self.wait(1)