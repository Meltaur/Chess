import pygame
from Squere import Squere 

class Board:
    board = []
    WHITE=(255, 255, 255)
    GREEN=(93,  179, 124)
    def __init__(self, surface) -> None:
        self.surface = surface
        for i in range(1,9):
            row = []
            for j in range(1,9):
                position = [464+(i-1)*64, 194+(j-1)*64]
                if (i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1):
                    row.append(Squere(self.surface, self.WHITE, position, 1, 'a'))
                else:
                    row.append(Squere(self.surface, self.GREEN, position, 1, 'a'))
            self.board.append(row)

    def draw(self):
        for i in range(8):
            for j in range(8):
                self.board[i][j].draw()


