import pygame
import sys

pygame.init()

tamanho_tela = pygame.display.set_mode((700, 400))
pygame.display.set_caption("MARIO_O_JOGO")

chao_img = pygame.image.load("/home/gustavo/Imagens/Captura de tela de 2026-10-06 01-54-33.png")
chao_img = pygame.transform.scale(chao_img, (700, 50))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    tamanho_tela.fill((135, 206, 235))

    pygame.draw.rect(tamanho_tela, (139, 69, 19), (0, 350, 700, 50))


    tamanho_tela.blit(chao_img, (0, 350))   


    pygame.display.flip()


pygame.quit()
