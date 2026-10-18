
# ==============================
# IMPORTAÇÕES
# ==============================
import pygame
import random


# ==============================
# CLASSE DO CENÁRIO
# ==============================
class Cenario:

    def __init__(self, largura_mapa=10100):

        self.largura_mapa = largura_mapa

        # ------------------------------
        # IMAGEM DO CHÃO
        # ------------------------------
        try:
            self.chao_img = pygame.image.load(
                "/home/gustavo/Imagens/Captura de tela de 2026-10-06 01-54-33.png"
            ).convert_alpha()

            self.chao_img = pygame.transform.scale(
                self.chao_img, (700, 50)
            )

        except Exception as e:
            print(f"FALHA CHÃO: {e}")
            self.chao_img = pygame.Surface((700, 50))
            self.chao_img.fill((0, 200, 0))

        # ------------------------------
        # IMAGEM DE FUNDO
        # ------------------------------
        try:
            fundo_original = pygame.image.load(
                "/home/gustavo/Imagens/file.enc"
            ).convert()

            altura_fundo = 400

            largura_original = fundo_original.get_width()
            altura_original = fundo_original.get_height()

            largura_fundo = int(
                largura_original * altura_fundo / altura_original
            )

            self.fundo_img = pygame.transform.scale(
                fundo_original,
                (largura_fundo, altura_fundo)
            )

        except Exception as e:
            print(f"FALHA FUNDO: {e}")

            self.fundo_img = pygame.Surface((700, 400))
            self.fundo_img.fill((92, 148, 252))

        # ------------------------------
        # IMAGENS DAS ÁRVORES
        # ------------------------------
        try:
            self.arvore1_img = pygame.image.load(
                "/home/gustavo/Imagens/ar1.png"
            ).convert_alpha()

            self.arvore2_img = pygame.image.load(
                "/home/gustavo/Imagens/ar2.png"
            ).convert_alpha()

            self.arvore1_img = pygame.transform.scale(
                self.arvore1_img, (110, 135)
            )

            self.arvore2_img = pygame.transform.scale(
                self.arvore2_img, (125, 135)
            )

        except Exception as e:
            print(f"FALHA ÁRVORES: {e}")

            self.arvore1_img = None
            self.arvore2_img = None

        # ------------------------------
        # IMAGEM DAS PEDRAS
        # ------------------------------
        try:
            pedra_img = pygame.image.load(
                "/home/gustavo/Imagens/imagem_pedra.png"
            ).convert_alpha()

            self.pedra_pequena = pygame.transform.scale(
                pedra_img, (30, 30)
            )

            self.pedra_media = pygame.transform.scale(
                pedra_img, (45, 45)
            )

            self.pedra_grande = pygame.transform.scale(
                pedra_img, (60, 60)
            )

        except Exception as e:
            print(f"FALHA PEDRAS: {e}")

            self.pedra_pequena = None
            self.pedra_media = None
            self.pedra_grande = None

        # ------------------------------
        # POSIÇÕES DAS ÁRVORES
        # ------------------------------
        self.arvores_cenario = []

        if self.arvore1_img and self.arvore2_img:

            x = 120

            while x < self.largura_mapa:
                x += random.randint(300, 480)

                if x >= self.largura_mapa:
                    break

                self.arvores_cenario.append((
                    random.choice([
                        self.arvore1_img,
                        self.arvore2_img
                    ]),
                    x,
                    350 - random.choice([
                        self.arvore1_img,
                        self.arvore2_img
                    ]).get_height() + 4
                ))

        # ------------------------------
        # POSIÇÕES DAS PEDRAS
        # ------------------------------
        self.pedras_cenario = []

        if self.pedra_pequena:

            x = 220

            while x < self.largura_mapa:
                x += random.randint(260, 420)

                if x >= self.largura_mapa:
                    break

                imagem = random.choice([
                    self.pedra_pequena,
                    self.pedra_media,
                    self.pedra_grande
                ])

                self.pedras_cenario.append((
                    imagem,
                    x,
                    350 - imagem.get_height() + 13
                ))

    # ==============================
    # DESENHAR O FUNDO
    # ==============================
    def desenhar_fundo(self, tela, camera):

        largura = self.fundo_img.get_width()

        if largura <= 0:
            return

        deslocamento = int(camera.x * 0.25) % largura
        inicio = -deslocamento

        for x in range(
            inicio - largura,
            tela.get_width() + largura,
            largura
        ):
            tela.blit(self.fundo_img, (x, 0))

    # ==============================
    # DESENHAR O CHÃO
    # ==============================
    def desenhar_chao(self, tela, camera):

        largura = self.chao_img.get_width()

        if largura <= 0:
            return

        deslocamento = int(camera.x) % largura
        inicio = -deslocamento

        for x in range(
            inicio - largura,
            tela.get_width() + largura,
            largura
        ):
            tela.blit(self.chao_img, (x, 350))

    # ==============================
    # DESENHAR AS ÁRVORES
    # ==============================
    def desenhar_arvores(self, tela, camera):

        for imagem, arvore_x, arvore_y in self.arvores_cenario:

            tela_x = arvore_x - camera.x

            if -imagem.get_width() < tela_x < tela.get_width():

                tela.blit(
                    imagem,
                    (int(tela_x), arvore_y)
                )

    # ==============================
    # DESENHAR AS PEDRAS
    # ==============================
    def desenhar_pedras(self, tela, camera):

        for imagem, pedra_x, pedra_y in self.pedras_cenario:

            tela_x = pedra_x - camera.x

            if -imagem.get_width() < tela_x < tela.get_width():

                tela.blit(
                    imagem,
                    (int(tela_x), pedra_y)
                )
