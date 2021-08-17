import pygame
class New_Menu:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((1440, 900))
        pygame.display.set_caption("Chess")
        icon = pygame.image.load('chess.png')
        pygame.display.set_icon(icon)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()

