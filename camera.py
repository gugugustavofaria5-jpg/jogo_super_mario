# ====================
# CÂMERA DO JOGO
# ====================

import pygame

# --------------------
# CONFIGURAÇÃO DA CÂMERA
# --------------------

class Camera:
    def __init__(self, largura_tela):
        self.x = 0
        self.largura_tela = largura_tela

    # ----------------------------
    # ATUALIZAR POSIÇÃO DA CÂMERA
    # ----------------------------

    def aplicar(self, retangulo):
        return retangulo.move(-self.x, 0)
