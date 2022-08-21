import pygame, sys
from settings import *

class Player:
    def __init__(self,pos,apple_random_pos):
        self.screen = pygame.display.get_surface()

        self.player_length = 1
        self.player_vec = pygame.math.Vector2()

        # create player rect
        self.player_rect = pygame.Rect(pos,(TILE_SIZE,TILE_SIZE)).inflate(-2,-2)
        self.player_rects = [self.player_rect]

        # func for randomize pos of apple
        self.apple_random_pos = apple_random_pos

        self.eat = False

    def check_game_over(self):
        if self.player_rect.left < 0 or self.player_rect.right > WIDTH or self.player_rect.top < 0 or self.player_rect.bottom > HEIGHT:
            return True
        for tail in self.player_rects[1::]:
            if self.player_rect.colliderect(tail) and self.eat == False:
                return True

    def add_next_rect(self,pos):
        if self.player_rects[-1]:
            self.player_rects.append(pygame.Rect(pos,(TILE_SIZE,TILE_SIZE)).inflate(-2,-2))

    def check_apple_collizion(self,apple):
        if self.player_rect.colliderect(apple.apple_rect):
            self.apple_random_pos(apple, self)
            self.player_length += 1
            self.add_next_rect((self.player_rects[-1].x-1, self.player_rects[-1].y-1))
            self.eat = True
        else:
            self.eat = False

    def check_input(self, event):
        if event == pygame.K_LEFT and self.player_vec.x != 1:
            self.player_vec.x = -1
            self.player_vec.y = 0
        elif event == pygame.K_RIGHT and self.player_vec.x != -1:
            self.player_vec.x = 1
            self.player_vec.y = 0
        elif event == pygame.K_UP and self.player_vec.y != 1:
            self.player_vec.x = 0
            self.player_vec.y = -1
        elif event == pygame.K_DOWN and self.player_vec.y != -1:
            self.player_vec.x = 0
            self.player_vec.y = 1

    def head_move(self):
        head = self.player_rects[0]
        head.x += self.player_vec[0] * TILE_SIZE
        head.y += self.player_vec[1] * TILE_SIZE

    def tail_move(self):
        i = -2
        for tail in reversed(self.player_rects[1::]):
            tail.x = self.player_rects[i].x
            tail.y = self.player_rects[i].y
            i -= 1              


    def update(self,apple):
        # move the tail before head for place first
        # tail rect next to head properly
        self.tail_move()

        # move the head
        self.head_move()
        
        # check if snake is eating apple
        self.check_apple_collizion(apple)

        # draw head and tail
        for rect in self.player_rects:
            pygame.draw.rect(self.screen,ORANGE,rect)
       
        # check if snake is out of window
        # self.check_game_over()

        