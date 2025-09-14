from manim import *

class Pesquisa(Scene):
    def construct(self):
        # Main text - the primary computer problem statement
        main_text = Text("Computador não está funcionando", color=YELLOW).scale(0.8)
        main_text.move_to(ORIGIN)
        
        # Create all text objects with fixed positions and colors
        text1 = Text("PC com erro", color=RED).scale(0.8)
        text1.move_to([-4, 2.5, 0])
        
        text2 = Text("Máquina não liga", color=GREEN).scale(0.8)
        text2.move_to([0, 2.5, 0])
        
        text3 = Text("Computador com problema", color=BLUE).scale(0.8)
        text3.move_to([4, 1.6, 0])
        
        text4 = Text("Equipamento com defeito", color=PURPLE).scale(0.8)
        text4.move_to([-3.6, -0.8, 0])
        
        text5 = Text("PC não responde", color=ORANGE).scale(0.8)
        text5.move_to([4, -1, 0])
        
        text6 = Text("Computador quebrado", color=TEAL).scale(0.8)
        text6.move_to([-4, -2.5, 0])
        
        text7 = Text("Máquina com falha", color=PINK).scale(0.8)
        text7.move_to([0, -1.5, 0])
        
        text8 = Text("Computador parou de funcionar", color=GOLD).scale(0.8)
        text8.move_to([3.8, -2.5, 0])
        
        text9 = Text("PC travado", color=MAROON).scale(0.8)
        text9.move_to([-3, 1.5, 0])
        
        text10 = Text("Máquina com bug", color=PURPLE_A).scale(0.8)
        text10.move_to([2, 1, 0])
        
        # Animation sequence - linear, no loops
        # First show the main text
        self.play(Write(main_text))
        self.wait(0.5)
        
        # Show each text with a fixed animation
        self.play(FadeIn(text1))
        self.play(FadeIn(text2))
        self.play(FadeIn(text3))
        self.play(FadeIn(text4))
        self.play(FadeIn(text5))
        self.play(FadeIn(text6))
        self.play(FadeIn(text7))
        self.play(FadeIn(text8))
        self.play(FadeIn(text9))
        self.play(FadeIn(text10))

        # Hold the final scene
        self.wait(2)