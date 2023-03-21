import pygame
import config

fps = config.FPS


class GameLoop:
    def __init__(self, clock, event_queue, renderer):
        self._clock = clock
        self._event_queue = event_queue
        self._renderer = renderer

    def start(self):
        while True:
            self._clock.tick(fps)
            self._handle_events()

            self._render()

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                exit()

    def _render(self):
        self._renderer.render()