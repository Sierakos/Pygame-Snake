import pygame, sys
from settings import *
from tile import *
from player import *
from apple import *
from random import randint

screen = pygame.display.set_mode((WIDTH,HEIGHT))
fps_clock = pygame.time.Clock()

def apple_random_pos(apple, player):
    if apple:
        apple.relocate((randint(1,MAP_WIDTH)*TILE_SIZE, randint(1,MAP_HEIGHT)*TILE_SIZE), player)

player_vec = pygame.math.Vector2()
player = Player((4*TILE_SIZE,4*TILE_SIZE), apple_random_pos)
apple = Apple((randint(1,MAP_WIDTH)*TILE_SIZE, randint(1,MAP_HEIGHT)*TILE_SIZE))

while True:
    for event in pygame.event.get():
        curr_time = pygame.time.get_ticks()
        if event.type == pygame.QUIT:
            sys.exit()
    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player_vec.x != 1:
                player_vec.x = -1
                player_vec.y = 0
            elif event.key == pygame.K_RIGHT and player_vec.x != -1:
                player_vec.x = 1
                player_vec.y = 0
            elif event.key == pygame.K_UP and player_vec.y != 1:
                player_vec.x = 0
                player_vec.y = -1
            elif event.key == pygame.K_DOWN and player_vec.y != -1:
                player_vec.x = 0
                player_vec.y = 1

    screen.fill(BLACK)

    for i in range(MAP_HEIGHT+1):
        for j in range(MAP_WIDTH+1):
            Tile((TILE_SIZE*j, TILE_SIZE*i))

    player.update(player_vec,apple)
    apple.update()
    pygame.display.update()
    fps_clock.tick(FPS)