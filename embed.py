from manim import *

class TextToVector(Scene):
    def construct(self):
        # Step 1: Input sentence
        sentence = Text('"EU GOSTO DE GATOS"', color=RED).scale(0.8).to_edge(UP)

        # Step 2: Arrow pointing down
        arrow1 = Arrow(start=UP, end=DOWN, color=RED).next_to(sentence, DOWN)

        # Step 3: Model box
        box = Rectangle(width=3, height=1.5, color=RED)
        box.next_to(arrow1, DOWN)
        model_text = Text("MODEL", color=RED).move_to(box.get_center())

        # Step 4: Arrow pointing to output
        arrow2 = Arrow(start=UP, end=DOWN, color=RED).next_to(box, DOWN)

        # Step 5: Output vector
        output = Text("[2, -1, 3]", color=RED).scale(0.8).next_to(arrow2, DOWN)

        # --- Animation sequence ---
        self.play(Write(sentence), run_time=0.5)
        self.wait(0.5)

        self.play(GrowArrow(arrow1), run_time=0.5)
        self.wait(0.5)

        self.play(Create(box), Write(model_text), run_time=0.5)
        self.wait(0.5)

        self.play(GrowArrow(arrow2), run_time=0.5)
        self.wait(0.5)

        self.play(Write(output), run_time=0.5)
        self.wait(1.5)


class TextBoxAnimation(Scene):
    def construct(self):
        # Create the text that will appear in the middle
        input_text = Text('"EU GOSTO DE GATOS"', color=RED).scale(1.2)
        
        # Create the model box on the right side
        model_box = Rectangle(width=3, height=2, color=RED)
        model_box.set_fill(RED, opacity=0.3)
        model_text = Text("MODEL", color=WHITE).scale(0.7).move_to(model_box.get_center())
        model_group = VGroup(model_box, model_text).to_edge(RIGHT, buff=1.5)
        
        # Create the output numbers
        output_numbers = Text("[2, -1, 3]", color=YELLOW).scale(0.8)
        
        # Animation sequence
        
        # 1. Show the text in the middle of the screen
        self.play(Write(input_text))
        self.wait(1)

        self.play(input_text.animate.scale(0.8).to_edge(LEFT))
        
        # 2. Show the model box on the right side
        self.play(Create(model_box), Write(model_text))
        self.wait(0.5)
        
        # 3. Create a vortex-like sucking effect
        start_point = input_text.get_center()
        end_point = model_box.get_center()
        
        # Create a vortex effect with particles
        vortex_dots = VGroup()
        num_dots = 12
        for i in range(num_dots):
            angle = i * 2 * PI / num_dots
            radius = 0.5
            dot = Dot(
                point=end_point + np.array([radius * np.cos(angle), radius * np.sin(angle), 0]),
                color=RED_A,
                radius=0.05
            )
            vortex_dots.add(dot)
        
        # Show the vortex forming
        self.play(FadeIn(vortex_dots))
        
        # Animate the vortex spinning
        self.play(
            Rotate(vortex_dots, angle=2*PI, about_point=end_point),
            run_time=1.0
        )
        
        # Move the text into the vortex with a spiral motion
        def spiral_path(t):
            # Spiral path from start to end
            angle = 3 * 2 * PI * t
            radius = (1 - t) * 2
            spiral_point = end_point + np.array([radius * np.cos(angle), radius * np.sin(angle), 0])
            # Blend between start and spiral
            return start_point * (1 - t) + spiral_point * t
        
        # Create the path
        spiral = VMobject()
        spiral.set_points_as_corners([spiral_path(t) for t in np.linspace(0, 1, 50)])
        
        # Play the spiral animation
        self.play(
            MoveAlongPath(input_text, spiral),
            input_text.animate.scale(0.4),
            rate_func=rush_into,
            run_time=1.5
        )
        
        # Make the text disappear into the vortex
        self.play(
            input_text.animate.scale(0.1).set_opacity(0),
            vortex_dots.animate.scale(0.1).set_opacity(0),
            rate_func=rush_into,
            run_time=0.8
        )
        self.wait(0.5)
        
        # 5. Move the box to the left side
        self.play(model_group.animate.to_edge(LEFT, buff=1.5))
        self.wait(0.5)
        
        # 6. Output the list of numbers from the box
        output_numbers.next_to(model_box, RIGHT)
        self.play(Write(output_numbers))
        self.wait(2)