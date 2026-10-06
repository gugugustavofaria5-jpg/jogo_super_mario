import pygame
import sys

pygame.init()

tamanho_tela = pygame.display.set_mode((700, 400))
pygame.display.set_caption("MARIO_O_JOGO")

chao_img = pygame.image.load("/home/gustavo/Imagens/Captura de tela de 2026-10-06 01-54-33.png")
chao_img = pygame.transform.scale(chao_img, (700, 50))

botao_esq = pygame.Rect(20, 300, 60, 60)
botao_dir = pygame.Rect(90, 300, 60, 60)
botao_pulo = pygame.Rect(580, 300, 60, 60)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    tamanho_tela.fill((135, 206, 235))

    pygame.draw.rect(tamanho_tela, (139, 69, 19), (0, 350, 700, 50))

    tamanho_tela.blit(chao_img, (0, 350))   

    pygame.display.flip()


    keys = pygame.key.get_pressed()

    mover_esq = False
    mover_dir = False
    pular = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.FINGERDOWN:

            x = int(event.x * 700)
            y = int(event.y * 400)
            if botao_esq.collidepoint(x, y):
                mover_esq = True
            if botao_dir.collidepoint(x, y):
                mover_dir = True
            if botao_pulo.collidepoint(x, y):
                botao_pulo = True

    if mover_esq:
        mario_x -= 5
    if mover_dir:
        mario_x += 5

    pygame.draw.rect(tamanho_tela, (200, 200, 200), botao_esq)
    pygame.draw.rect(tamanho_tela, (200, 200, 200), botao_dir)
    pygame.draw.rect(tamanho_tela, (200, 200, 200), botao_pulo)

pygame.quit()
