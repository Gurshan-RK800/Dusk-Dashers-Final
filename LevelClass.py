import pygame
from Config import *


class Level():
    def __init__(self,displaySurface):

        self.skyImage = pygame.image.load(SPRITESHEET_PATH + "Background/Background.png").convert()
        self.skyImage = pygame.transform.scale(self.skyImage, (window_width, window_height))

        self.displaySurface = displaySurface

    def update(self):
        pass

    def draw(self):
        self.displaySurface.blit(self.skyImage, (0, 0))

    def run(self):
        self.update()
        self.draw()

