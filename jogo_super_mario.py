import pygame

pygame.init()

tamanho_tela = pygame.display.set_mode((700, 400))
pygame.display.set_caption("MARIO_O_JOGO")

chao_img = pygame.image.load("/home/gustavo/Imagens/Captura de tela de 2026-10-06 01-54-33.png")
chao_img = pygame.transform.scale(chao_img, (700, 50))

mario_img = pygame.image.load("/home/gustavo/Imagens/imagem do mario.png")
mario_img = pygame.transform.scale(mario_img, (30, 40))

mario_x = 300
mario_y = 310

mario_vel_y = 0
GRAVIDADE = 0.8
FORCA_PULO = -15
mario_no_chao = False

mario_dir = 1

botao_esq = pygame.Rect(20, 300, 60, 60)
botao_dir = pygame.Rect(90, 300, 60, 60)
botao_pulo = pygame.Rect(580, 300, 60, 60)

running = True
while running:
    mover_esq = False
    mover_dir = False
    pular = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.FINGERDOWN:

            if mover_esq:
                mario_dir = -1
            if mario_dir:
                mario_dir = 1

            if mario_dir == -1:
                mario_flip = pygame.transform.flip(mario_img, True, False)
                tamanho_tela.blit(mario_flip, (mario_x, mario_y))
            else:
                tamanho_tela.blit(mario_img, (mario_x, mario_y))


            x = int(event.x * 700)
            y = int(event.y * 400)
            if botao_esq.collidepoint(x, y):
                mover_esq = True
            if botao_dir.collidepoint(x, y):
                mover_dir = True
            if botao_pulo.collidepoint(x, y):
                pular = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            mover_esq = True
        if keys[pygame.K_RIGHT]:
            mover_dir = True
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            pular = True

    if mover_esq:
        mario_x -= 5
    if mover_dir:
        mario_x += 5

    if pular and mario_no_chao:
        mario_vel_y = FORCA_PULO
        mario_no_chao = False

    mario_vel_y += GRAVIDADE
    mario_y += mario_vel_y

    mario_no_chao = False
    if mario_y + 40 >= 350:
        mario_y = 350 - 40
        mario_vel_y = 0
        mario_no_chao = True

    tamanho_tela.fill((135, 206, 235))
    pygame.draw.rect(tamanho_tela, (139, 69, 19), (0, 350, 700, 50))
    tamanho_tela.blit(chao_img, (0, 350))
    tamanho_tela.blit(mario_img, (mario_x, mario_y))   
    pygame.draw.rect(tamanho_tela, (200, 200, 200), botao_esq)
    pygame.draw.rect(tamanho_tela, (200, 200, 200), botao_dir)
    pygame.draw.rect(tamanho_tela, (200, 200, 200), botao_pulo)

    pygame.display.flip()


pygame.quit()
