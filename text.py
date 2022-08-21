import pygame
from settings import *

def show_score(score):
    screen = pygame.display.get_surface()
    font = pygame.font.SysFont('arial', 20)
    score = font.render(f'Score: {score}', True, BLACK)
    score_rect = score.get_rect(topleft = (0,0))
    screen.blit(score,score_rect)

def menu_text():
    screen = pygame.display.get_surface()
    font = pygame.font.SysFont('arial', 20)
    start = font.render(f'Press space to start', True, BLACK)
    start_rect = start.get_rect(center = (WIDTH // 2, HEIGHT // 2))
    screen.blit(start,start_rect)

def over_text(score):
    screen = pygame.display.get_surface()
    font = pygame.font.SysFont('arial', 20)
    start = font.render(f'Your score: {score} press space to try again', True, BLACK)
    start_rect = start.get_rect(center = (WIDTH // 2, HEIGHT // 2))
    screen.blit(start,start_rect)

