import pygame
from settings import *

class Apple:
    def __init__(self,pos):
        self.screen = pygame.display.get_surface()

        # create apple rect
        self.apple_rect = pygame.Rect(pos,(TILE_SIZE,TILE_SIZE)).inflate(-2,-2)

    def relocate(self, pos):
        self.apple_rect = pygame.Rect(pos,(TILE_SIZE,TILE_SIZE)).inflate(-2,-2)

    def update(self):
        # draw rect
        pygame.draw.rect(self.screen,RED,self.apple_rect)