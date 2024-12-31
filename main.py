import pygame
from Config import *
from LevelClass import Level

pygame.init()
clock = pygame.time.Clock()

displaySurface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Dusk Dashers')

level = Level(displaySurface)


isGameRunning = True
while isGameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isGameRunning = False
    level.run()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()