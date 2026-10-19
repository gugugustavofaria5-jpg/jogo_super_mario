
# ==============================
# MAPA DO JOGO
# FASE 1 - PLANICIE VERDE
# ==============================

import pygame

# ==============================
# CONFIGURAÇÃO DA FASE
# ==============================

LARGURA_MAPA = 10100
ALTURA_CHAO = 350


# ==============================
# CRIAR PLATAFORMAS
# ==============================

def criar_plataformas():

    plataformas = [

        # ÁREA 1 - INÍCIO
        pygame.Rect(180, 275, 120, 30),
        pygame.Rect(340, 225, 80, 30),
        pygame.Rect(455, 185, 120, 30),

        # ÁREA 2 - PRIMEIROS SALTOS
        pygame.Rect(780, 270, 120, 30),
        pygame.Rect(950, 230, 80, 30),
        pygame.Rect(1060, 185, 120, 30),
        pygame.Rect(1240, 225, 160, 30),
        pygame.Rect(1450, 275, 120, 30),

        # ÁREA 3 - SUBIDA E DESCIDA
        pygame.Rect(1780, 255, 120, 30),
        pygame.Rect(1940, 215, 120, 30),
        pygame.Rect(2100, 170, 80, 30),
        pygame.Rect(2220, 135, 120, 30),
        pygame.Rect(2400, 195, 160, 30),
        pygame.Rect(2610, 265, 120, 30),

        # ÁREA 4 - CAMINHO ALTERNATIVO
        pygame.Rect(2810, 285, 160, 30),
        pygame.Rect(3000, 245, 120, 30),
        pygame.Rect(3160, 200, 80, 30),
        pygame.Rect(3280, 160, 120, 30),
        pygame.Rect(3470, 205, 160, 30),

        # ÁREA 5 - PLATAFORMAS EM GRUPOS
        pygame.Rect(3800, 270, 120, 30),
        pygame.Rect(3970, 230, 120, 30),
        pygame.Rect(4130, 185, 120, 30),
        pygame.Rect(4320, 225, 160, 30),
        pygame.Rect(4540, 275, 120, 30),

        # ÁREA 6 - COLINA
        pygame.Rect(4800, 260, 120, 30),
        pygame.Rect(4960, 220, 80, 30),
        pygame.Rect(5080, 180, 120, 30),
        pygame.Rect(5250, 140, 120, 30),
        pygame.Rect(5450, 195, 160, 30),

        # ÁREA 7 - CAMINHO IRREGULAR
        pygame.Rect(5700, 240, 120, 30),
        pygame.Rect(5880, 280, 160, 30),
        pygame.Rect(6120, 245, 120, 30),
        pygame.Rect(6290, 205, 80, 30),
        pygame.Rect(6410, 165, 120, 30),
        pygame.Rect(6600, 245, 160, 30),

        # ÁREA 8 - SEQUÊNCIA DE SALTOS
        pygame.Rect(6870, 220, 120, 30),
        pygame.Rect(7050, 175, 120, 30),
        pygame.Rect(7230, 225, 160, 30),

        # ÁREA 9
        pygame.Rect(7500, 275, 120, 30),
        pygame.Rect(7680, 235, 80, 30),
        pygame.Rect(7800, 190, 120, 30),
        pygame.Rect(7990, 230, 160, 30),

        # ÁREA 10
        pygame.Rect(8270, 270, 120, 30),
        pygame.Rect(8450, 225, 120, 30),
        pygame.Rect(8620, 180, 80, 30),
        pygame.Rect(8740, 145, 120, 30),
        pygame.Rect(8930, 215, 160, 30),

        # ÁREA 11
        pygame.Rect(9200, 270, 120, 30),
        pygame.Rect(9380, 230, 80, 30),
        pygame.Rect(9500, 185, 120, 30),
        pygame.Rect(9690, 225, 160, 30),
        pygame.Rect(9900, 270, 120, 30),

    ]

    return plataformas


# ==============================
# CRIAR CANOS
# ==============================

def criar_canos():

    canos = [

        pygame.Rect(620, 290, 60, 60),
        pygame.Rect(1080, 270, 60, 80),
        pygame.Rect(1640, 280, 60, 70),
        pygame.Rect(2330, 260, 60, 90),
        pygame.Rect(2740, 290, 60, 60),
        pygame.Rect(3610, 280, 60, 70),
        pygame.Rect(4650, 260, 60, 90),
        pygame.Rect(5350, 280, 60, 70),
        pygame.Rect(5620, 270, 60, 80),
        pygame.Rect(6800, 260, 60, 90),
        pygame.Rect(7440, 280, 60, 70),
        pygame.Rect(8170, 250, 60, 100),
        pygame.Rect(9070, 280, 60, 70),
        pygame.Rect(9820, 270, 60, 80),

    ]
    return canos
# ==============================
# CRIAR GRAMA DO CENÁRIO
# ==============================

def criar_grama():

    import random

    gramas = []
    x = 40

    while x < LARGURA_MAPA - 100:

        gramas.append(
            (x, ALTURA_CHAO - 40)
        )

        # Menor intervalo = mais grama
        x += random.randint(100, 180)

    return gramas


# ==============================
# CRIAR SEGUNDA GRAMA DO CENÁRIO
# ==============================

def criar_grama_2(altura=60):

    import random

    gramas = []
    x = 100

    while x < LARGURA_MAPA - 100:

        # Ajuste vertical da segunda grama
        AJUSTE_ALTURA = 29

        gramas.append(
            (x, ALTURA_CHAO - altura - AJUSTE_ALTURA)
        )

        # Espaçamento menor para aumentar a quantidade
        x += random.randint(180, 280)

    return gramas