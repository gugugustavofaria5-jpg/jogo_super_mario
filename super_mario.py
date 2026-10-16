# ==============================
# IMPORTAÇÃO E INICIALIZAÇÃO
# ==============================
import pygame
from mapa import criar_plataformas

pygame.init()
clock = pygame.time.Clock()
# ==============================
# CONFIGURAÇÃO DA TELA
# ==============================
tamanho_tela = pygame.display.set_mode((700, 400))
pygame.display.set_caption("MARIO_O_JOGO")

# ==============================
# CARREGAMENTO DAS IMAGENS
# ==============================


chao_img = pygame.image.load("/home/gustavo/Imagens/Captura de tela de 2026-10-06 01-54-33.png")
chao_img = pygame.transform.scale(chao_img, (700, 50))

mario_img = pygame.image.load("/home/gustavo/Imagens/imagem de mario 2.0.webp")
mario_img = pygame.transform.scale(mario_img, (30, 40))

# ==============================
# IMAGEM DOS BLOCOS
# ==============================
bloco_img = pygame.image.load(
    "/home/gustavo/Imagens/bloco.png"
).convert_alpha()

bloco_img = pygame.transform.scale(bloco_img, (40, 30))

# ==============================
# VARIÁVEIS DO MARIO
# ==============================

mario_x = 300
mario_y = 310
mario_vel_x = 0
mario_vel_y = 0

mario_no_chao = False
mario_dir = 1
pulo_pressionado = False


# ==============================
# CONFIGURAÇÕES DA MOVIMENTAÇÃO
# ==============================

ACEL = 0.45
FRICAO = 0.80
VEL_MAX = 4.5
ACEL_AR = 0.25

GRAVIDADE = 0.45
GRAVIDADE_QUEDA = 0.75
FORCA_PULO = -11
VEL_QUEDA_MAX = 12
CORTE_PULO = 0.45

# ==============================
# BOTÕES DE CONTROLE
# ==============================

botao_esq = pygame.Rect(20, 300, 60, 60)
botao_dir = pygame.Rect(90, 300, 60, 60)
botao_pulo = pygame.Rect(580, 300, 60, 60)

# ==============================
# LOOP PRINCIPAL DO JOGO
# ==============================

running = True

# ------------------------------
# PLATAFORMAS Do MAPA
# ------------------------------
plataformas = criar_plataformas()

while running:

    # ------------------------------
    # ESTADO DOS CONTROLES
    # ------------------------------

    mover_esq = False
    mover_dir = False
    pular = False

    # ------------------------------
    # CAPTURA DOS EVENTOS
    # ------------------------------￼

    for event in pygame.event.get():

        # Fechar o jogo
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_UP, pygame.K_SPACE):
                if mario_vel_y < 0:
                    mario_vel_y *= CORTE_PULO
                    
        # Detectar toques na tela
        if event.type == pygame.FINGERDOWN:
            x = int(event.x * 700)
            y = int(event.y * 400)
            if botao_esq.collidepoint(x, y):
                mover_esq = True
            if botao_dir.collidepoint(x, y):                  
                mover_dir = True
            if botao_pulo.collidepoint(x, y):
                pular = True

    # ------------------------------
    # CONTROLES DO TECLADO
    # ------------------------------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mover_esq = True
    if keys[pygame.K_RIGHT]:
        mover_dir = True
    if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
        pular = True

    aceleracao_atual = ACEL if mario_no_chao else ACEL_AR

    # ------------------------------
    # MOVIMENTAÇÃO HORIZONTAL
    # ------------------------------

    if mover_esq:
        mario_vel_x -= aceleracao_atual
        mario_dir = -1

    elif mover_dir:
        mario_vel_x += aceleracao_atual
        mario_dir = 1

    else:
        if mario_no_chao:
            mario_vel_x *= FRICAO
        else:
            mario_vel_x *= 0.98
            

    # Limitar velocidade horizontal
    mario_vel_x = max(-VEL_MAX, min(VEL_MAX, mario_vel_x))

    if abs(mario_vel_x) < 0.05 and not mover_esq and not mover_dir:
        mario_vel_x = 0

    # Atualizar posição horizontal

    #Limitar velocidade horizotal
    mario_x += mario_vel_x

    mario_x = max(0, min(700 - 30, mario_x))

    #Atualizar posição horizontal
    mario_x = max(0, min(700 - 30, mario_x))

    # ------------------------------
    # PULO DO MARIO
    # ------------------------------

    if pular and mario_no_chao:
        mario_vel_y = FORCA_PULO
        mario_no_chao = False

    # ------------------------------
    # GRAVIDADE E VELOCIDADE DE QUEDA
    # ------------------------------

    # Guardar a posição anterior para detectar pousos
    mario_y_anterior = mario_y

    if mario_vel_y < 0:
        mario_vel_y += GRAVIDADE
    else:
        mario_vel_y += GRAVIDADE_QUEDA

    #Limitar a velocidade máxima da queda
    mario_vel_y = min(mario_vel_y, VEL_QUEDA_MAX)

    #Atualizar posição vertical
    mario_y += mario_vel_y

    # ------------------------------
    # COLISÃO COM AS PLATAFORMAS
    # ------------------------------
    
    mario_no_chao = False

    mario_rect = pygame.Rect(mario_x, mario_y, 30, 40)
    mario_rect_anterior = pygame.Rect(
        mario_x, mario_y_anterior, 30, 40
    )

    for plataforma in plataformas:

        #Verificar se o Mario está caindo
        if mario_vel_y >= 0:

            # Verificar se os pés cruzaram o topo do bloco
            if (
                mario_rect_anterior.bottom <= plataforma.top
                and mario_rect.bottom >= plataforma.top
                and mario_rect.right > plataforma.left
                and mario_rect.left < plataforma.right
            ):
                mario_y = plataforma.top - 40
                mario_vel_y = 0
                mario_no_chao = True

                # Atualizar o retângulo após o pouso
                mario_rect.y = mario_y


    # ------------------------------
    # COLISÃO COM O CHÃO
    # ------------------------------

    if mario_y + 40 >= 350:
        mario_y = 310
        mario_vel_y = 0
        mario_no_chao = True

    # ------------------------------
    # DESENHAR O CENÁRIO
    # ------------------------------

    tamanho_tela.fill((135, 206, 235))
    pygame.draw.rect(tamanho_tela, (139, 69, 19), (0, 350, 700, 50))
    tamanho_tela.blit(chao_img, (0, 350))

    # ------------------------------
    # DESENAHR BLOCOS
    # ------------------------------
    for plataforma in plataformas:
        for x in range(plataforma.left, plataforma.right, 40):
            tamanho_tela.blit(bloco_img, (x, plataforma.y))

    # ------------------------------
    # DESENHAR O MARIO
    # ------------------------------

    if mario_dir == -1:
        mario_flip = pygame.transform.flip(mario_img, True, False)
        tamanho_tela.blit(mario_flip, (mario_x, mario_y))
    else:
        tamanho_tela.blit(mario_img, (mario_x, mario_y))

    # ------------------------------
    # DESENHAR OS BOTÕES
    # ------------------------------

    pygame.draw.rect(tamanho_tela, (200, 200, 200), botao_esq)
    pygame.draw.rect(tamanho_tela, (200, 200, 200), botao_dir)
    pygame.draw.rect(tamanho_tela, (200, 200, 200), botao_pulo)

    # ------------------------------
    # ATUALIZAR O JOGO
    # ------------------------------

    clock.tick(60)
    pygame.display.flip()

# ==============================
# ENCERRAR O PYGAME
# ==============================
pygame.quit()
