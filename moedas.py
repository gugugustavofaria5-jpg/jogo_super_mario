
import pygame


class Moedas:
    """Gerencia as moedas, a coleta e a pontuação do jogo."""

    def __init__(self):
        # ==============================
        # CONFIGURAÇÃO
        # ==============================
        self.tamanho = 20
        self.pontuacao = 0

        # ==============================
        # POSIÇÕES DAS MOEDAS NO MAPA
        # ==============================
        self.posicoes = [
            # Primeiro grupo
            (400, 280), (440, 250), (480, 280),
            (520, 250), (560, 280), (600, 250),
            (640, 280), (680, 250), (720, 280),

            # Sequência de moedas no ar
            (820, 280), (860, 250), (900, 220),
            (940, 250), (980, 280), (1020, 250),
            (1060, 220), (1100, 250), (1140, 280),

            # Grupo seguinte
            (1300, 280), (1340, 240), (1380, 200),
            (1420, 240), (1460, 280), (1500, 240),
            (1540, 200), (1580, 240), (1620, 280),

            # Fileira longa
            (1750, 280), (1800, 280), (1850, 280),
            (1900, 280), (1950, 280), (2000, 280),
            (2050, 280), (2100, 280), (2150, 280),

            # Moedas em formato de arco
            (2300, 280), (2340, 240), (2380, 200),
            (2420, 180), (2460, 200), (2500, 240),
            (2540, 280),

            # Região seguinte
            (2700, 260), (2740, 220), (2780, 180),
            (2820, 220), (2860, 260), (2900, 220),
            (2940, 180), (2980, 220), (3020, 260),

            # Mais moedas pelo mapa
            (3200, 280), (3250, 250), (3300, 220),
            (3350, 250), (3400, 280),
            (3600, 280), (3650, 280), (3700, 280),
            (3750, 280), (3800, 280),

            # Outro arco
            (4000, 280), (4040, 240), (4080, 200),
            (4120, 180), (4160, 200), (4200, 240),
            (4240, 280),

            # Continuação do mapa
            (4450, 260), (4500, 220), (4550, 180),
            (4600, 220), (4650, 260),
            (4850, 280), (4900, 240), (4950, 200),
            (5000, 240), (5050, 280),

            # Moedas adicionais
            (5300, 280), (5350, 280), (5400, 280),
            (5450, 280), (5500, 280),
            (5750, 260), (5800, 220), (5850, 180),
            (5900, 220), (5950, 260),

            # Últimos grupos
            (6200, 280), (6250, 240), (6300, 200),
            (6350, 240), (6400, 280),
            (6700, 280), (6750, 280), (6800, 280),
            (6850, 280), (6900, 280),
        ]


        self.criar_moedas()

    # ==============================
    # CRIAR MOEDAS
    # ==============================
    def criar_moedas(self):
        self.moedas = [
            pygame.Rect(x, y, self.tamanho, self.tamanho)
            for x, y in self.posicoes
        ]

    # ==============================
    # DESENHAR MOEDAS
    # ==============================
    def desenhar(self, tela, camera):
        for moeda in self.moedas:
            moeda_tela = camera.aplicar(moeda)

            pygame.draw.ellipse(
                tela, (150, 95, 0), moeda_tela
            )

            parte_interna = moeda_tela.inflate(-4, -2)

            pygame.draw.ellipse(
                tela, (255, 205, 35),parte_interna
            )

            pygame.draw.line(
                tela,
                (255, 245, 150),
                (moeda_tela.centerx, moeda_tela.top + 4),
                (moeda_tela.centerx, moeda_tela.bottom - 4),
                2,
            )

    # ==============================
    # COLETAR MOEDAS
    # ==============================
    def verificar_coleta(self, retangulo_mario):
        coletadas = 0

        for moeda in self.moedas[:]:
            if retangulo_mario.colliderect(moeda):
                self.moedas.remove(moeda)
                self.pontuacao += 1
                coletadas += 1

        return coletadas

    # ==============================
    # REINICIAR
    # ==============================

    def reiniciar(self):
        self.pontuacao = 0
        self.criar_moedas()
        