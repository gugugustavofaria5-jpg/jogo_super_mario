
import pygame


class Checkpoint:
    def __init__(self, x, y, caminho_imagem, tamanho=(80, 120)):
        self.x = x
        self.y = y
        self.ativado = False

        self.imagem = pygame.image.load(
            caminho_imagem
        ).convert_alpha()

        self.imagem = pygame.transform.scale(
            self.imagem, tamanho
        )

        self.rect = pygame.Rect(
            x, y, tamanho[0], tamanho[1]
        )

    def verificar_ativacao(self, mario_rect):
        if not self.ativado and self.rect.colliderect(mario_rect):
            self.ativado = True
            return True

        return False

    def desenhar(self, tela, camera):
        posicao_tela = camera.aplicar(self.rect)
        tela.blit(self.imagem, posicao_tela)
        