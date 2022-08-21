import pygame, sys
from settings import *
from tile import *
from player import *
from apple import *
from random import randint
from text import *

class Game:
    def __init__(self):


        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Snake')
        self.fps_clock = pygame.time.Clock()

        self.player = Player((4*TILE_SIZE,4*TILE_SIZE), self.apple_random_pos)
        self.apple = Apple((randint(1,MAP_WIDTH)*TILE_SIZE, randint(1,MAP_HEIGHT)*TILE_SIZE))

    def apple_random_pos(self, apple, player):
        if apple:
            apple.relocate((randint(1,MAP_WIDTH)*TILE_SIZE, randint(1,MAP_HEIGHT)*TILE_SIZE), player)

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
                if event.type == pygame.KEYDOWN:
                    self.player.check_input(event.key)

            self.screen.fill(BLACK)

            for i in range(MAP_HEIGHT+1):
                for j in range(MAP_WIDTH+1):
                    Tile((TILE_SIZE*j, TILE_SIZE*i))
            
            show_score(self.player.player_length)
            self.player.update(self.apple)
            self.apple.update()
            pygame.display.update()
            if self.player.check_game_over():
                self.game_over(self.player.player_length)
            self.fps_clock.tick(FPS)

    def menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.run()

            self.screen.fill(BLACK)

            for i in range(MAP_HEIGHT+1):
                for j in range(MAP_WIDTH+1):
                    Tile((TILE_SIZE*j, TILE_SIZE*i))

            menu_text()
            pygame.display.update()
            self.fps_clock.tick(FPS)

    def game_over(self, score):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player = None
                        self.apple = None
                        self.player = Player((4*TILE_SIZE,4*TILE_SIZE), self.apple_random_pos)
                        self.apple = Apple((randint(1,MAP_WIDTH)*TILE_SIZE, randint(1,MAP_HEIGHT)*TILE_SIZE))
                        self.run()

            self.screen.fill(BLACK)

            for i in range(MAP_HEIGHT+1):
                for j in range(MAP_WIDTH+1):
                    Tile((TILE_SIZE*j, TILE_SIZE*i))

            over_text(score)
            pygame.display.update()
            self.fps_clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.menu()