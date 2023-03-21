import pygame

class Square(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, value=0):
        super().__init__()

        self.sqr_size = 120
        self.rect = pygame.Rect(x, y, self.sqr_size, self.sqr_size)
        self.rect.x = x
        self.rect.y = y
        self.value = value

    def grow(self):
        self.value *= 2