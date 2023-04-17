import sys
import pygame
import move


class GameLoop:
    def __init__(self, clock, event_queue, renderer, board):
        self._clock = clock
        self._event_queue = event_queue
        self._renderer = renderer
        self._board = board

    def start(self):
        # GAME STARTS WITH TWO SQUARES FILLED ALREADY
        self._board.spawn_square()
        self._board.spawn_square()

        self.print_list()

        while True:
            self._clock.tick()
            self._handle_events()
            self._render()

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # RESTART THE GAME
                if event.key == pygame.K_ESCAPE:
                    self._board.reset()

                # ADD NUMBERS ON DEMAND, FOR MANUAL TESTING PURPOSES
                if event.key == pygame.K_SPACE:
                    self._board.spawn_square()
                    self.print_list()

                # MOVES SQUARES UP
                if event.key in [pygame.K_UP, pygame.K_w]:
                    move.up(self._board)
                    self.print_list()

                # MOVE SQUARES DOWN
                if event.key in [pygame.K_DOWN, pygame.K_s]:
                    move.down(self._board)
                    self.print_list()

                # MOVE SQUARES LEFT
                if event.key in [pygame.K_LEFT, pygame.K_a]:
                    move.left(self._board)
                    self.print_list()

                # MOVE SQUARES RIGHT
                if event.key in [pygame.K_RIGHT, pygame.K_d]:
                    move.right(self._board)
                    self.print_list()

    def _render(self):
        self._renderer.render()

    # FOR DEVELOPMENT ONLY (WILL BE DELETED LATER)
    def print_list(self):
        self._board.update_list()
        for i in self._board.list:
            print(i)
        print()
