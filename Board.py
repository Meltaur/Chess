import pygame
from Squere import Squere 

class Board:
    board = []
    flag = True
    WHITE=(255, 255, 255)
    GREEN=(93,  179, 124)
    def __init__(self, surface) -> None:
        self.surface = surface
        for i in range(1,9):
            row = []
            for j in range(1,9):
                position = [464+(i-1)*64, 194+(j-1)*64]
                if self.flag:
                    row.append(Squere(self.surface, self.WHITE, position, 1, 'a'))
                    self.flag = False
                else:
                    row.append(Squere(self.surface, self.GREEN, position, 1, 'a'))
                    self.flag = True
            self.board.append(row)

    def draw(self):
        for i in range(8):
            for j in range(8):
                self.board[i][j].draw()


