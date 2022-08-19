import pygame
from settings import *

class Tile:
    def __init__(self,pos):
        self.screen = pygame.display.get_surface()
        # create rect
        background_rect = pygame.Rect(pos,(TILE_SIZE,TILE_SIZE))
        border_rect = pygame.Rect(pos,(TILE_SIZE,TILE_SIZE))

        # draw rect
        pygame.draw.rect(self.screen,GREEN,background_rect)
        pygame.draw.rect(self.screen,BLUE,border_rect,1)