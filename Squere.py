import pygame

class Squere:
    def __init__(self, surface, color, position,letter,number):
        self.color = color
        self.surface = surface
        self.position = position
        self.letter=letter
        self.number=number


    def draw(self):
        pygame.draw.rect(self.surface, self.color, [self.position[0], self.position[1], 64, 64])