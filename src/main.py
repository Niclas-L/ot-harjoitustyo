import pygame
import config
from clock import Clock
from game_loop import GameLoop
from event_queue import EventQueue
from renderer import Renderer

# A lot of the framework currently present is inspired by pygame-sokoban at:
# https://github.com/ohjelmistotekniikka-hy/pygame-sokoban/blob/4b9937166bbcd3adc7dc6522fcf898b90400926a/src/event_queue.py


def main():

    win = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    pygame.display.set_caption("2048")

    clock = Clock()
    event_queue = EventQueue()
    renderer = Renderer(win)
    game_loop = GameLoop(clock, event_queue, renderer)

    pygame.init()
    game_loop.start()






if __name__ == '__main__':
    main()