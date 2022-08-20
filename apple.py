import pygame
from settings import *
from random import randint

class Apple:
    def __init__(self,pos):
        self.screen = pygame.display.get_surface()

        # create apple rect
        self.apple_rect = pygame.Rect(pos,(TILE_SIZE,TILE_SIZE)).inflate(-2,-2)

    def relocate(self, pos, player):
        self.apple_rect = pygame.Rect(pos,(TILE_SIZE,TILE_SIZE)).inflate(-2,-2)
        for rect in player.player_rects:
            if self.apple_rect.colliderect(rect):
                self.relocate((randint(1,MAP_WIDTH)*TILE_SIZE, randint(1,MAP_HEIGHT)*TILE_SIZE), player)

    def update(self):
        # draw rect
        pygame.draw.rect(self.screen,RED,self.apple_rect)