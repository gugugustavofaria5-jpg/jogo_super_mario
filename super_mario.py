# ==============================
# IMPORTAÇÃO E INICIALIZAÇÃO
# ==============================
import pygame
from mapa import criar_plataformas, criar_canos
from camera import Camera

pygame.init()
clock = pygame.time.Clock()
# ==============================
# CONFIGURAÇÃO DA TELA
# ==============================
tamanho_tela = pygame.display.set_mode((700, 400))
pygame.display.set_caption("MARIO_O_JOGO")

# ==============================
# CÂMERA DO JOGO
# ==============================

camera = Camera(700)

# ==============================
# CARREGAMENTO DAS IMAGENS
# ==============================
try:
    chao_img = pygame.image.load("/home/gustavo/Imagens/Captura de tela de 2026-10-06 01-54-33.png").convert_alpha()
    chao_img = pygame.transform.scale(chao_img, (700, 50))
except Exception as e:
    print(f"FALHA CHÃO: {e}")
    chao_img = pygame.Surface((700, 50))
    chao_img.fill((0, 200, 0))

# Cópia espelhada (seu código original preservado)
chao_img_espelhado = pygame.transform.flip(chao_img, True, False)

try:
    mario_img = pygame.image.load("/home/gustavo/Imagens/imagem de mario 2.0.webp").convert_alpha()
    mario_img = pygame.transform.scale(mario_img, (30, 40))
except Exception as e:
    print(f"FALHA MARIO: {e}")
    mario_img = pygame.Surface((30, 40))
    mario_img.fill((255, 0, 0))

# ==============================
# IMAGEM DOS BLOCOS
# ==============================
try:
    bloco_img = pygame.image.load("/home/gustavo/Imagens/bloco.png").convert_alpha()
    bloco_img = pygame.transform.scale(bloco_img, (40, 30))
except Exception as e:
    print(f"FALHA BLOCO: {e}")
    bloco_img = pygame.Surface((40, 30))
    bloco_img.fill((200, 100, 0))

# ==============================
# IMAGEM DE FUNDO
# ==============================
try:
    fundo_original = pygame.image.load("/home/gustavo/Imagens/file.enc").convert()
    altura_fundo = 400
    largura_original = fundo_original.get_width()
    altura_original = fundo_original.get_height()
    largura_fundo = int(largura_original * altura_fundo / altura_original)
    fundo_img = pygame.transform.scale(fundo_original, (largura_fundo, altura_fundo))
except Exception as e:
    print(f"FALHA FUNDO file.enc: {e} - usando fundo azul temporário")
    fundo_img = pygame.Surface((700, 400))
    fundo_img.fill((92, 148, 252))

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
# PLATAFORMAS DO MAPA
# ------------------------------
plataformas = criar_plataformas()
canos = criar_canos

# ------------------------------
# DESENHAR CANOS VERDES
# ------------------------------

for cano in canos:
    cano_tela = camera.aplicar(cano)

    # Corpo do cano
    pygame.draw.rect(
        tamanho_tela,
        (0, 150, 30),
        cano_tela
    )

    # Borda externa 
    pygame.draw.rect(
        tamanho_tela,
        (0, 90, 20),
        cano_tela,
        3
    )

    # Parte superior do cano
    topo_cano = pygame.Rect(
        cano_tela.x - 5,
        cano_tela.y,
        cano_tela.width + 10,
        15
    )

    pygame.draw.rect(
        tamanho_tela,
        (0, 200, 40),
        topo_cano
    )

    pygame.draw.rect(
        tamanho_tela,
        (0, 100, 20),
        topo_cano,
        3
    )

    #Reflexo luz no lado esquerdo 
    pygame.draw.line(
        (100, 255, 100),
        (cano_tela.x + 8, cano_tela.y + 18),
        (cano_tela.x + 8, cano_tela.bottom - 5),
        4
    )

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

    if mario_x < 0:
        mario_x = 0

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

    for plataforma in plataformas + canos:

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
    # ATUALIZAR A CÂMERA
    # ------------------------------

    camera.atualizar(mario_x)


    # ==============================
    # DESENHAR O FUNDO PANORÂMICO
    # ==============================
    velocidade_parallax = 0.25
    fundo_largura = fundo_img.get_width()

    if fundo_largura > 0:
        deslocamento_fundo = int(camera.x * velocidade_parallax) % fundo_largura
        fundo_x = -deslocamento_fundo

        for x in range(
            fundo_x - fundo_largura,
            tamanho_tela.get_width() + fundo_largura,
            fundo_largura
        ):
            tamanho_tela.blit(fundo_img, (x, 0))
        
        # ==============================
        # DESENHAR CHÃO CONTÍNUO
        # ==============================
        chao_largura = chao_img.get_width()
        if chao_largura > 0:
            deslocamento_chao = int(camera.x) % chao_largura
            chao_x = -deslocamento_chao

            for x in range(
                chao_x - chao_largura,
                tamanho_tela.get_width() + chao_largura,
                chao_largura
            ):
                tamanho_tela.blit(chao_img, (x, 350))

        # ------------------------------
        # DESENAHR BLOCOS
        # ------------------------------
        
        for plataforma in plataformas:
            plataforma_tela = camera.aplicar(plataforma)

            for x in range(plataforma_tela.left, plataforma_tela.right, 40):
                tamanho_tela.blit(bloco_img, (x, plataforma_tela.y))

        # ------------------------------
        # DESENHAR O MARIO
        # ------------------------------
        mario_tela_x = int(mario_x - camera.x)
        if mario_dir == -1:
            mario_flip = pygame.transform.flip(mario_img, True, False)
            tamanho_tela.blit(mario_flip, (mario_tela_x, mario_y))
        else:
            tamanho_tela.blit(mario_img, (mario_tela_x, mario_y))

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
