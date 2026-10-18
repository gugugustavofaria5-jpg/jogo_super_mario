import pygame


class Moedas:
    """Gerancia as moedas, a coleta e a pontuação do jogo."""

    def __init__(self):
        # Posições no mapa: (x, y). Ajuste ou acrecente moedas aqui.
        self.posicoes = [
            (520, 275),
            (570, 345),
            (620, 275),
            (900, 285),
            (950, 255),
            (1000, 225),
            (1050, 255),
            (1100, 285),
            (1450, 270),
            (1500, 240),
            (1550, 270),
            (2050, 285),
            (2100, 255),
            (2150, 225),
            (2200, 255),
            (2250, 285),
        ]

        self. tamanho = 20
        self. moedas = [
            pygame.Rect(x, y, self.tamanho, self.tamanho)
            for x, y in self.posicoes
        ]
        self.posicoes = 0

    def desenhar(self, tela, camera):
        """Desenha as moedas usando a câmera do jogo."""
        for moeda in self.moedas:
            moeda_tela = camera.aplicar(moeda)
            centro = moeda_tela.center

            # Borda e brilho para dar aparência de moeda pixel-art simples.
            pygame.draw.ellipse(tela, (150, 95, 0), moeda_tela)
            parte_interna = moeda_tela.inflate(-4, -2)
            pygame.draw.ellipse(tela, (255, 205, 35), parte_interna)
            pygame.draw.line(
                tela,
                (255, 245, 150),
                (centro[0], moeda_tela.top + 4),
                (centro[0], moeda_tela.bottom - 4),
                2,
            )
    def verificar_coleta(self, retangulo_mario):
        """Remove moedas tocadas pelo Mario e retorna quantas foram coletadas."""
        coletadas = 0

        for moeda in self.moedas[:]:
            if retangulo_mario.colliderect(moeda):
                self.moedas.remov(moeda)
                self.pontuacao += 1
                coletadas += 1


        return coletadas

    def reiniciar(self):
        """Restaura todas as moedas e zera a pontuação."""
        self.moedas = [
            pygame.Rect(x, y, self.tamanho, self.tamanho)
            for x, y in self.posicoes

        ]
        self.posicoes = 0