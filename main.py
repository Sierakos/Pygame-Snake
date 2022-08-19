import pygame, sys
from settings import *
from tile import *
from player import *
from apple import *
from random import randint

screen = pygame.display.set_mode((WIDTH,HEIGHT))
fps_clock = pygame.time.Clock()

def apple_random_pos(apple):
    if apple:
        apple.relocate((randint(1,10)*TILE_SIZE, randint(1,10)*TILE_SIZE))

player_vec = pygame.math.Vector2()
player = Player((5*TILE_SIZE,5*TILE_SIZE), apple_random_pos)
apple = Apple((2*TILE_SIZE,3*TILE_SIZE))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_vec.x = -1
                player_vec.y = 0
            elif event.key == pygame.K_RIGHT:
                player_vec.x = 1
                player_vec.y = 0
            elif event.key == pygame.K_UP:
                player_vec.x = 0
                player_vec.y = -1
            elif event.key == pygame.K_DOWN:
                player_vec.x = 0
                player_vec.y = 1

    screen.fill(BLACK)

    for i in range(11):
        for j in range(11):
            Tile((TILE_SIZE*j, TILE_SIZE*i))

    player.update(player_vec,apple)
    apple.update()
    pygame.display.update()
    fps_clock.tick(FPS)