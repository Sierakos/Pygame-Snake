import pygame, sys
from settings import *

class Player:
    def __init__(self,pos,apple_random_pos):
        self.screen = pygame.display.get_surface()

        self.player_length = 1

        # create player rect
        self.player_rect = pygame.Rect(pos,(TILE_SIZE,TILE_SIZE)).inflate(-2,-2)
        self.player_rects = [self.player_rect, self.player_rect]

        # func for randomize pos of apple
        self.apple_random_pos = apple_random_pos

        # wait 1 tick for next tail
        self.move_last_tail = True

    def check_game_over(self):
        if self.player_rect.left < 0 or self.player_rect.right > WIDTH or self.player_rect.top < 0 or self.player_rect.bottom > HEIGHT:
            sys.exit()

    def add_next_rect(self,pos):
        if self.player_rects[-1]:
            self.player_rects.append(pygame.Rect(pos,(TILE_SIZE,TILE_SIZE)).inflate(-2,-2))

    def check_apple_collizion(self,apple):
        if self.player_rect.colliderect(apple.apple_rect):
            self.apple_random_pos(apple)
            self.player_length += 1
            self.add_next_rect((self.player_rects[-1].x-1, self.player_rects[-1].y-1))
            self.move_last_tail = False
        else:
            self.move_last_tail = True

        print(self.move_last_tail)
        print(self.player_rects)

    def head_move(self,player_vec):
        head = self.player_rects[0]
        head.x += player_vec[0] * TILE_SIZE
        head.y += player_vec[1] * TILE_SIZE
        # pygame.draw.rect(self.screen,ORANGE,head)

    def tail_move(self,apple):
        if len(self.player_rects) > 2:
            i = -1
            for tail in reversed(self.player_rects[2::]):
                tail.x = self.player_rects[i-1].x
                tail.y = self.player_rects[i-1].y
                # self.player_rects[i].x = self.player_rects[i-1].x 
                # self.player_rects[i].y = self.player_rects[i-1].y 
                i -= 1

                    

    def update(self,player_vec,apple):
        # check if snake is eating apple
        self.check_apple_collizion(apple)
        # move the head
        self.head_move(player_vec)
        self.tail_move(apple)

        for rect in self.player_rects:
            pygame.draw.rect(self.screen,ORANGE,rect)
       
        # check if snake is out of window
        self.check_game_over()

        