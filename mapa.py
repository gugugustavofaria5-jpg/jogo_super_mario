# =========================
# MAPA DO JOGO
# FASE 1 - PLANICIE VERDE
# =========================

import pygame

# =========================
# COMFIGURAÇÃO DA FASE
# =========================

LARGURA_MAPA = 7000
ALTURA_CHAO = 350


# =================================
# PLATAFORMAS DA PRIMEIRA REGIÃO
# =================================

def criar_paltaformas():

    paltaformas = [

        # ----------------------------
        # AREA 1 - INICIO DA AVENTURA
        # ----------------------------

        pygame.Rect(150, 270, 120, 30),
        pygame.Rect(330, 220, 120, 30),
        pygame.Rect(500, 170, 120, 30),

        # -------------------------------
        # AREA 2 - PRIMEIRAS EXPLORAÇÕES
        # -------------------------------

        pygame.Rect(750, 270, 120, 30),
        pygame.Rect(950, 220, 120, 30),
        pygame.Rect(1150, 170, 120, 30),
        pygame.Rect(1350, 230, 160, 30),
        pygame.Rect(1550, 270, 120, 30),

        # ------------------------------
        # AREA 3 - CAMINHO ELEVADO
        # ------------------------------

        pygame.Rect(1800, 240, 120, 30),
        pygame.Rect(1960, 200, 120, 30),
        pygame.Rect(2120, 160, 120, 30),
        pygame.Rect(2300, 200, 160, 30),
        pygame.Rect(2500, 250, 120, 30),

        # ------------------------------
        # AREA 4 - CAMINHO ALTERNATIVO
        # ------------------------------

        pygame.Rect(2750, 280, 160, 30),
        pygame.Rect(2950, 240, 120, 30),
        pygame.Rect(3120, 200, 120, 30),
        pygame.Rect(3300, 160, 120, 30),
        pygame.Rect(3480, 210, 160, 30),

        # ------------------------------
        # AREA 5 - PLATAFORMAS DISTANTES
        # ------------------------------

        pygame.Rect(3750, 260, 120, 30),
        pygame.Rect(3930, 220, 120, 30),
        pygame.Rect(4110, 180, 120, 30),
        pygame.Rect(4290, 220, 160, 30),
        pygame.Rect(4500, 270, 120, 30),

        # ------------------------------
        # AREA 6 - CAMINHO DA COLINA
        # ------------------------------

        pygame.Rect(4750, 250, 120, 30),
        pygame.Rect(4910, 210, 120, 30),
        pygame.Rect(5070, 170, 120, 30),
        pygame.Rect(5230, 130, 120, 30),
        pygame.Rect(5420, 180, 160, 30),

        # ------------------------------
        # AREA 7 - APROXIMACAO DO FINAL
        # ------------------------------

        pygame.Rect(5650, 230, 120, 30),
        pygame.Rect(5830, 270, 160, 30),
        pygame.Rect(6080, 240, 120, 30),
        pygame.Rect(6270, 200, 120, 30),
        pygame.Rect(6460, 250, 160, 30),

        # ------------------------------
        # AREA 8 - ULTIMO TRECHO
        # ------------------------------

        pygame.Rect(6700, 220, 120, 30),
        pygame.Rect(6880, 180, 120, 30),

    ]
    return paltaformas
