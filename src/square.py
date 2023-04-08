import pygame


class Square(pygame.sprite.Sprite):
    def __init__(self, key):
        super().__init__()

        # NOT CONCERNING MYSELF WITH GRAPHICS UNTIL CORE GAME LOOP WORKS IN CONSOLE
        # self.sqr_size = 120
        # self.rect = pygame.Rect(x, y, self.sqr_size, self.sqr_size)
        self._value = 0
        self._key = key

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
