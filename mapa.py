# =========================
# MAPA DO JOGO
# =========================

import pygame


# -------------------------
# PLATAFORMAS DE TIJOLOS
# -------------------------

def criar_plataformas():
    plataformas= [
        pygame.Rect(150, 270, 120, 30),
        pygame.Rect(330, 220, 120, 30),
        pygame.Rect(500, 170, 120, 30),
    ]

    return plataformas

