from manim import *

class PesquisandoBanco(Scene):
    def construct(self):
        # Definimos as palavras e seus vetores correspondentes
        palavras = {
            "REI": [4, 2],
            "RAINHA": [3, 1],
            "CACHORRO": [1, 5],
            "GATO": [2, 4],
            "CASTELO": [4, 1]
        }
        
        # Palavra que será animada
        palavra_animada = "CASTELO"
        
        # Cores para cada palavra
        cores = {
            "REI": RED,
            "RAINHA": PURPLE,
            "CACHORRO": BLUE,
            "GATO": GREEN,
            "CASTELO": ORANGE
        }
        
        # Parte do modelo - na esquerda e funcionando na vertical
        box = Rectangle(width=1.7, height=1, color=cores[palavra_animada])
        box.move_to(ORIGIN).to_edge(LEFT, buff=1.0)  # Posição fixa na esquerda
        model_text = Text("MODEL", color=cores[palavra_animada]).scale(0.6).move_to(box.get_center())
        
        # Setas para a palavra animada
        arrow_in = Arrow(start=UP, end=DOWN, color=cores[palavra_animada])
        arrow_out = Arrow(start=UP, end=DOWN, color=cores[palavra_animada])
        
        # Espaço vetorial com eixos x e y de 0 a 5 - à direita do modelo
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            axis_config={"color": BLUE},
            x_length=6,
            y_length=6
        )
        
        # Posicionando os eixos à direita do modelo
        axes.to_edge(RIGHT, buff=2)
        
        # Adicionando rótulos aos eixos
        x_label = Text("x", color=BLUE).scale(0.7).next_to(axes.x_axis.get_end(), RIGHT)
        y_label = Text("y", color=BLUE).scale(0.7).next_to(axes.y_axis.get_end(), UP)
        
        # Adicionando números aos eixos
        x_numbers = VGroup()
        for i in range(6):
            num = Text(str(i), color=BLUE).scale(0.4)
            num.next_to(axes.c2p(i, 0), DOWN, buff=0.2)
            x_numbers.add(num)
        
        y_numbers = VGroup()
        for i in range(6):
            num = Text(str(i), color=BLUE).scale(0.4)
            num.next_to(axes.c2p(0, i), LEFT, buff=0.2)
            y_numbers.add(num)
        
        # Criar pontos e rótulos para todas as palavras no espaço vetorial
        pontos = {}
        rotulos = {}
        
        for palavra, coordenadas in palavras.items():
            # Criar ponto no espaço vetorial
            pontos[palavra] = Dot(axes.c2p(coordenadas[0], coordenadas[1]), color=cores[palavra])
            
            # Criar rótulo para o ponto
            rotulos[palavra] = Text(palavra, color=cores[palavra]).scale(0.5)
            rotulos[palavra].next_to(pontos[palavra], UP+RIGHT, buff=0.1)
        
        # Primeiro mostrar o modelo, os eixos e todas as palavras já no espaço vetorial
        self.play(Create(box), Write(model_text))
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Write(x_numbers), Write(y_numbers))
        
        # Adicionar todas as palavras exceto a que será animada
        for palavra in palavras.keys():
            if palavra != palavra_animada:
                self.play(
                    FadeIn(pontos[palavra]),
                    FadeIn(rotulos[palavra]),
                    run_time=0.3
                )
        
        # Agora animar apenas a palavra escolhida
        # Texto de entrada acima da caixa
        texto_entrada = Text(f'"{palavra_animada}"', color=cores[palavra_animada]).scale(0.7)
        texto_entrada.next_to(box, UP, buff=2)
        
        # Posicionando as setas
        arrow_in.next_to(box, UP, buff=0.2)
        arrow_out.next_to(box, DOWN, buff=0.2)
        
        # Vetor de saída abaixo da seta
        coordenadas = palavras[palavra_animada]
        vetor_saida = Text(f"[{coordenadas[0]}, {coordenadas[1]}]", color=cores[palavra_animada]).scale(0.7)
        vetor_saida.next_to(arrow_out, DOWN, buff=0.2)

        self.wait(2)
        
        # Animação da palavra escolhida
        self.play(Write(texto_entrada), run_time=0.8)
        self.play(GrowArrow(arrow_in), run_time=0.8)
        self.wait(0.3)
        self.play(GrowArrow(arrow_out), run_time=0.8)
        self.play(Write(vetor_saida), run_time=0.8)
        self.wait(0.3)
        
        # Mostrar o ponto e animar a transformação do vetor para o rótulo
        self.play(FadeIn(pontos[palavra_animada]), run_time=0.8)
        vetor_saida_copia = vetor_saida.copy()

        pontos[palavra_animada] = Dot(axes.c2p(coordenadas[0], coordenadas[1]), color=cores[palavra_animada])
        rotulos[palavra_animada] = Text(palavra_animada, color=cores[palavra_animada]).scale(0.5)
        rotulos[palavra_animada].next_to(pontos[palavra_animada], DOWN+RIGHT, buff=0.1)

        self.play(Transform(vetor_saida_copia, rotulos[palavra_animada]), run_time=1.2)

        self.wait(2)
        
        # Adicionar um círculo vermelho em volta da palavra CASTELO
        circulo = Circle(color=RED, stroke_width=5, radius=1.4)
        circulo.move_to(pontos[palavra_animada])
        circulo.shift(UP*0.25)
        circulo.shift(LEFT*0.2)
        self.play(Create(circulo), run_time=0.8)

        
        # Manter a cena final
        self.wait(2)