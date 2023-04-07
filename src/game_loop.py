import pygame
import config

fps = config.FPS


class GameLoop:
    def __init__(self, clock, event_queue, renderer, board):
        self._clock = clock
        self._event_queue = event_queue
        self._renderer = renderer
        self._board = board

    def start(self):

        while True:
            self._clock.tick(fps)
            self._handle_events()

            # Not bothering with graphics until core game loop works in console
            # self._render()

    def _handle_events(self):
        self.keys_pressed = pygame.key.get_pressed()
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self._board.spawn_square()
                    print(self._board.list)

    def _render(self):
        self._renderer.render()
