import pygame
class New_Menu:
    def __init__(self):

        self.screen = pygame.display.set_mode((1440, 900))
        pygame.display.set_caption("Chess")
        self.icon = pygame.image.load('chess.png')
        pygame.display.set_icon(self.icon)

    def screen_color(self):
        self.screen.fill((169,169,169))
        