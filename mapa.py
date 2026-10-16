# =========================
# MAPA DO JOGO
# =========================

import pygame


# -------------------------
# PLATAFORMAS DE TIJOLOS
# -------------------------

def criar_plataformas():
    plataformas= [
        # ---------------------------
        # PRIMEIRA PARTE DO MAPA
        # ---------------------------

        pygame.Rect(150, 270, 120, 30),
        pygame.Rect(330, 220, 120, 30),
        pygame.Rect(500, 170, 120, 30),

        # ----------------------------
        # NOVOS PLATAFORMAS
        # ----------------------------
        pygame.Rect(750, 270, 120, 30),
        pygame.Rect(950, 220, 120, 30),
        pygame.Rect(1150, 170, 120, 30),
        pygame.Rect(1400, 170, 120, 30),
        pygame.Rect(1600, 200, 120, 30),
    ]

    return plataformas

