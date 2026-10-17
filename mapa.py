# =========================
# MAPA DO JOGO
# FASE 1 - PLANICIE VERDE
# =========================

import pygame

# =========================
# COMFIGURAÇÃO DA FASE
# =========================

LARGURA_MAPA = 10100
ALTURA_CHAO = 350


# =================================
# PLATAFORMAS DA PRIMEIRA REGIÃO
# =================================

def criar_plataformas():

    plataformas = [

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

        # Região 9
        pygame.Rect(7000, 270, 120, 30),
        pygame.Rect(7180, 230, 120, 30),
        pygame.Rect(7360, 190, 120, 30),
        pygame.Rect(7540, 240, 160, 30),

        # Região 10
        pygame.Rect(7800, 270, 120, 30),
        pygame.Rect(7980, 220, 120, 30),
        pygame.Rect(8160, 170, 120, 30),
        pygame.Rect(8340, 210, 160, 30),

        # Região 11
        pygame.Rect(8600, 260, 120, 30),
        pygame.Rect(8780, 220, 120, 30),
        pygame.Rect(8960, 180, 120, 30),
        pygame.Rect(9140, 230, 160, 30),

        # Região 12
        pygame.Rect(9400, 270, 120, 30),
        pygame.Rect(9580, 220, 120, 30),
        pygame.Rect(9760, 170, 120, 30),
        pygame.Rect(9940, 210, 160, 30),

    ]
    return plataformas

# ========================
# CANOS NO MAPA
# ========================

def criar_canos():

    canos = [
        # Primeiro cano
        pygame.Rect(600, 290, 60, 60),

        # Segundo cano
        pygame.Rect(1050, 270, 60, 80),

        # Terceiro cano
        pygame.Rect(1700, 280, 60, 70),

        # Quarto cano
        pygame.Rect(2650, 260, 60, 90),

        # Quinto cano
        pygame.Rect(3650, 280, 60, 70),

        # Sexto cano
        pygame.Rect(4650, 260, 60, 90),

        # Sétimo cano
        pygame.Rect(5600, 280, 60, 70),

        # Último cano
        pygame.Rect(6600, 270, 60, 80),

        # =======================
        # NOVOS CANOS
        # =======================

        pygame.Rect(7200, 270, 60, 80),
        pygame.Rect(7900, 250, 60, 100),
        pygame.Rect(8500, 280, 60, 70),
        pygame.Rect(9250, 260, 60, 90),
        pygame.Rect(9850, 270, 60, 80),
    ]
    return canos
