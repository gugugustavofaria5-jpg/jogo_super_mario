
import pygame


class MenuCheckpoint:
    def __init__(self):
        self.fonte_titulo = pygame.font.Font(None, 46)
        self.fonte_texto = pygame.font.Font(None, 30)
        self.fonte_botao = pygame.font.Font(None, 32)

        self.botao_continuar = pygame.Rect(
            230, 300, 240, 55
        )

    def desenhar(self, tela, pontuacao):
        sombra = pygame.Surface((700, 400), pygame.SRCALPHA)
        sombra.fill((0, 0, 20, 210))
        tela.blit(sombra, (0, 0))

        painel = pygame.Rect(130, 35, 440, 335)

        pygame.draw.rect(tela, (25, 35, 65), painel)
        pygame.draw.rect(tela, (60, 210, 255), painel, 4)

        titulo = self.fonte_titulo.render(
            "CHECKPOINT!", True, (100, 230, 255)
        )
        tela.blit(
            titulo,
            titulo.get_rect(center=(350, 85))
        )

        texto = self.fonte_texto.render(
            f"Moedas: {pontuacao}", True, (255, 230, 90)
        )
        tela.blit(texto, (190, 155))

        texto_inimigos = self.fonte_texto.render(
            "Inimigos derrotados: 0", True, (255, 255, 255)
        )
        tela.blit(texto_inimigos, (190, 200))

        pygame.draw.rect(
            tela, (30, 150, 100),
            self.botao_continuar, border_radius=8
        )

        texto_botao = self.fonte_botao.render(
            "CONTINUAR", True, (255, 255, 255)
        )

        tela.blit(
            texto_botao,
            texto_botao.get_rect(
                center=self.botao_continuar.center
            )
        )

    def verificar_clique(self, posicao):
        return self.botao_continuar.collidepoint(posicao)
    