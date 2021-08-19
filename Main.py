from Menu import New_Menu
from Board import Board
import pygame

def main():
    pygame.init()

    #Deklaracja obiektów
    menu = New_Menu()
    board = Board(menu.screen)

    running = True
    
    #Pętla główna
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        menu.screen_color()
        board.draw()
        pygame.display.update()


if __name__ == '__main__':
    main()