import pygame
import config


class Square(pygame.sprite.Sprite):
    def __init__(self, key, x_coord, y_coord):
        super().__init__()

        self._value = 0
        self._key = key
        self.create_rect(x_coord, y_coord)

    def __repr__(self):
        return str(self.get_value())

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def grow(self):
        self._value *= 2

    def reset(self):
        self._value = 0

    # CREATES PYGAME RECT OBJECT FOR THE SQUARE, USED IN RENDERER
    def create_rect(self, x_coord, y_coord):
        self.rect = pygame.Rect(
            x_coord, y_coord, config.SQUARE_SIZE, config.SQUARE_SIZE)
