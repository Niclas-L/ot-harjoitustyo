import pygame
import config


class Renderer:
    def __init__(self, win):
        self._win = win

    def render(self):
        self._win.fill(config.BG_COLOR)
        pygame.display.flip()
