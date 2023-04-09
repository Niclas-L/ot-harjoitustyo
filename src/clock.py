import pygame
import config


class Clock:
    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self):
        self._clock.tick(config.FPS)

    def get_ticks(self):
        return pygame.time.get_ticks()
