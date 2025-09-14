from manim import *

class BancoVetorial(Scene):
    def construct(self):
        
        # Parte do modelo - agora na esquerda e funcionando na vertical
        # Primeiro definimos a caixa do modelo como ponto principal e fixo
        box = Rectangle(width=1.7, height=1, color=RED)
        box.move_to(ORIGIN).to_edge(LEFT, buff=1.0)  # Posição fixa na esquerda
        model_text = Text("MODEL", color=RED).scale(0.6).move_to(box.get_center())
        
        # Definimos as palavras e seus vetores correspondentes
        palavras = {
            "REI": [4, 2],
            "RAINHA": [3, 1],
            "CACHORRO": [1, 5],
            "GATO": [2, 4]
        }
        
        # Cores para cada palavra
        cores = {
            "REI": RED,
            "RAINHA": PURPLE,
            "CACHORRO": BLUE,
            "GATO": GREEN
        }
        
        # Setas apontando para cima e para baixo (serão reutilizadas)
        arrow_in = Arrow(start=UP, end=DOWN, color=WHITE)
        arrow_out = Arrow(start=UP, end=DOWN, color=WHITE)
        
        # Espaço vetorial com eixos x e y de 0 a 5 - agora à direita do modelo
        # Criando os eixos
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
        
        # Agrupando o espaço vetorial
        vector_space = VGroup(axes, x_label, y_label, x_numbers, y_numbers)
        
        # Criar pontos e rótulos para cada palavra no espaço vetorial
        pontos = {}
        rotulos = {}
        
        for palavra, coordenadas in palavras.items():
            # Criar ponto no espaço vetorial
            pontos[palavra] = Dot(axes.c2p(coordenadas[0], coordenadas[1]), color=cores[palavra])
            
            # Criar rótulo para o ponto
            rotulos[palavra] = Text(palavra, color=cores[palavra]).scale(0.5)
            rotulos[palavra].next_to(pontos[palavra], UP+RIGHT, buff=0.1)
        
        # Sequência de animação
        # Primeiro mostrar os elementos do espaço vetorial
        self.play(Create(box), Write(model_text))
        self.play(FadeIn(axes), FadeIn(x_label), FadeIn(y_label), FadeIn(x_numbers), FadeIn(y_numbers))
        
        # Para cada palavra, mostrar a animação
        for palavra, coordenadas in palavras.items():
            # Posicionar setas e textos
            texto_entrada = Text(f'"{palavra}"', color=cores[palavra]).scale(0.7)
            
            # Posicionar texto de entrada acima da caixa
            texto_entrada.next_to(box, UP, buff=2)
            
            # Seta de entrada (de cima para baixo)
            arrow_in_atual = arrow_in.copy().set_color(cores[palavra])
            arrow_in_atual.next_to(box, UP, buff=0.2)
            
            # Seta de saída (de cima para baixo)
            arrow_out_atual = arrow_out.copy().set_color(cores[palavra])
            arrow_out_atual.next_to(box, DOWN, buff=0.2)
            
            # Vetor de saída abaixo da seta
            vetor_saida = Text(f"[{coordenadas[0]}, {coordenadas[1]}]", color=cores[palavra]).scale(0.7)
            vetor_saida.next_to(arrow_out_atual, DOWN, buff=0.2)
            
            # Mostrar a palavra de entrada
            self.play(FadeIn(texto_entrada), run_time=0.5)
            self.play(GrowArrow(arrow_in_atual), run_time=0.5)
            self.play(GrowArrow(arrow_out_atual), run_time=0.5)
            self.play(FadeIn(vetor_saida), run_time=0.5)
            
            # Mostrar o ponto correspondente
            self.play(FadeIn(pontos[palavra]), run_time=0.5)
            
            # Animar o texto saindo do modelo e indo para o ponto no espaço vetorial
            vetor_saida_copia = vetor_saida.copy()
            self.play(Transform(vetor_saida_copia, rotulos[palavra]), run_time=0.5)
            
            # Limpar para a próxima palavra (exceto a última)
            if palavra != list(palavras.keys())[-1]:
                self.play(
                    FadeOut(texto_entrada),
                    FadeOut(arrow_in_atual),
                    FadeOut(arrow_out_atual),
                    FadeOut(vetor_saida),
                    run_time=0.5
                )
        
        # Manter a cena final
        self.wait(2)