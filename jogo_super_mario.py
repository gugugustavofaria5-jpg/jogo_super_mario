import pygame

pygame.init()

tamanho_tela = pygame.display.set_mode((700, 400))
pygame.display.set_caption("MARIO_O_JOGO")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
