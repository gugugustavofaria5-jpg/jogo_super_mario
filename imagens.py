
# ==============================
# CARREGAMENTO CENTRAL DAS IMAGENS
# ==============================

from pathlib import Path
import pygame

# Pasta onde ficam as imagens do jogo
PASTA_IMAGENS = Path(__file__).resolve().parent / "assets"


def carregar_imagem(nome):
    caminho = PASTA_IMAGENS / nome

    if not caminho.is_file():
        raise FileNotFoundError(
            f"Imagem não encontrada: {caminho}"
        )

    return pygame.image.load(str(caminho)).convert_alpha()


# ==============================
# IMAGEM DO CHÃO
# ==============================

try:
    chao_img = pygame.transform.scale(
        carregar_imagem("chao.png"), (700, 50)
    )
except Exception as e:
    print(f"FALHA CHÃO: {e}")
    chao_img = pygame.Surface((700, 50))
    chao_img.fill((0, 200, 0))

chao_img_espelhado = pygame.transform.flip(
    chao_img, True, False
)


# ==============================
# IMAGEM DO MARIO
# ==============================

try:
    mario_img = pygame.transform.scale(
        carregar_imagem("imagem_mario.png"), (30, 40)
    )
except Exception as e:
    print(f"FALHA MARIO: {e}")
    mario_img = pygame.Surface((30, 40))
    mario_img.fill((255, 0, 0))


# ==============================
# IMAGEM DOS BLOCOS
# ==============================

try:
    bloco_img = pygame.transform.scale(
        carregar_imagem("bloco.png"), (40, 30)
    )
except Exception as e:
    print(f"FALHA BLOCO: {e}")
    bloco_img = pygame.Surface((40, 30))
    bloco_img.fill((200, 100, 0))


# ==============================
# IMAGEM DOS CANOS
# ==============================

cano_img = carregar_imagem("tobo_mario.png")


# ==============================
# IMAGEM DE FUNDO
# ==============================

try:
    fundo_original = pygame.image.load(
        str(PASTA_IMAGENS / "fundo.enc")
    ).convert()

    altura_fundo = 400
    largura_original = fundo_original.get_width()
    altura_original = fundo_original.get_height()

    largura_fundo = int(
        largura_original * altura_fundo / altura_original
    )

    fundo_img = pygame.transform.scale(
        fundo_original,
        (largura_fundo, altura_fundo)
    )

except Exception as e:
    print(f"FALHA FUNDO: {e} - usando fundo azul temporário")
    fundo_img = pygame.Surface((700, 400))
    fundo_img.fill((92, 148, 252))


# ==============================
# IMAGENS DAS ARVORES
# ==============================

arvore1_img = pygame.transform.scale(
    carregar_imagem("ar1.png"), (165, 203)
)

arvore2_img = pygame.transform.scale(
    carregar_imagem("ar2.png"), (188, 204)
)


# ==============================
# IMAGEM DAS PEDRAS
# ==============================

pedra_img = carregar_imagem("imagem_pedra.png")

pedra_pequena = pygame.transform.scale(
    pedra_img, (30, 30)
)

pedra_media = pygame.transform.scale(
    pedra_img, (45, 45)
)

pedra_grande = pygame.transform.scale(
    pedra_img, (60, 60)
)


# ==============================
# IMAGENS DA GRAMA
# ==============================

imagem_grama = pygame.transform.scale(
    carregar_imagem("imagem_grama.png"), (100, 40)
)

imagem_grama_2 = carregar_imagem("imagem_grama_2.png")

LARGURA_GRAMA_2 = 100
altura_original = imagem_grama_2.get_height()
largura_original = imagem_grama_2.get_width()

ALTURA_GRAMA_2 = int(
    altura_original * LARGURA_GRAMA_2 / largura_original
)

imagem_grama_2 = pygame.transform.scale(
    imagem_grama_2,
    (LARGURA_GRAMA_2, ALTURA_GRAMA_2)
)
