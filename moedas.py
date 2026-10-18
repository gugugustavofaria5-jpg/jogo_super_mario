
import pygame


class Moedas:
    """Gerencia a criação, a coleta e a pontuação das moedas."""

    def __init__(self, plataformas=None):
        # ==============================
        # CONFIGURAÇÕES
        # ==============================
        self.tamanho = 20
        self.espacamento = 65
        self.distancia_topo = 5
        self.pontuacao = 0

        self.posicoes = []
        self.moedas = []

        # Guarda uma cópia das posições iniciais para reiniciar.
        self.configurar_plataformas(plataformas or [])

    # ==============================
    # GERAR MOEDAS NAS PLATAFORMAS
    # ==============================
    def configurar_plataformas(self, plataformas):
        self.posicoes = []
        self.moedas = []

        posicoes_usadas = set()

        for plataforma in plataformas:
            # Aceitar somente retângulos válidos.
            if not isinstance(plataforma, pygame.Rect):
                continue

            if plataforma.width < self.tamanho:
                continue

            if plataforma.height <= 0:
                continue

            # Altura: moeda acima da plataforma.
            y = plataforma.top - self.tamanho - self.distancia_topo

            # Distribuir moedas ao longo da plataforma.
            margem = min(
                10,
                max(0, (plataforma.width - self.tamanho) // 2)
            )

            x_inicial = plataforma.left + margem
            x_final = plataforma.right - margem - self.tamanho

            if x_final < x_inicial:
                continue

            largura_util = x_final - x_inicial

            if largura_util == 0:
                candidatos = [x_inicial]
            else:
                quantidade = max(
                    2,
                    largura_util // self.espacamento + 1
                )

                candidatos = [
                    round(
                        x_inicial
                        + i * largura_util / (quantidade - 1)
                    )
                    for i in range(quantidade)
                ]

            for x in candidatos:
                # Evitar posições duplicadas.
                chave = (int(x), int(y))

                if chave in posicoes_usadas:
                    continue

                moeda = pygame.Rect(
                    int(x),
                    int(y),
                    self.tamanho,
                    self.tamanho
                )

                # Garantir que a moeda fique dentro da área
                # horizontal da plataforma.
                if moeda.left < plataforma.left:
                    continue

                if moeda.right > plataforma.right:
                    continue

                posicoes_usadas.add(chave)
                self.posicoes.append(chave)
                self.moedas.append(moeda)

    # ==============================
    # DESENHAR MOEDAS
    # ==============================
    def desenhar(self, tela, camera):
        for moeda in self.moedas:
            moeda_tela = camera.aplicar(moeda)
            centro = moeda_tela.center

            pygame.draw.ellipse(
                tela, (150, 95, 0), moeda_tela
            )

            parte_interna = moeda_tela.inflate(-4, -2)

            pygame.draw.ellipse(
                tela, (255, 205, 35), parte_interna
            )

            pygame.draw.line(
                tela,
                (255, 245, 150),
                (centro[0], moeda_tela.top + 4),
                (centro[0], moeda_tela.bottom - 4),
                2
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
    # REINICIAR MOEDAS
    # ==============================
    def reiniciar(self):
        self.pontuacao = 0

        self.moedas = [
            pygame.Rect(x, y, self.tamanho, self.tamanho)
            for x, y in self.posicoes
        ]
