import pygame
from Character import Player

pygame.init()

screen_width = 1200
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: quit()

pygame.quit()