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

            # NOT BOTHERING WITH GRAPHICS UNTIL CORE GAME LOOP WORKS IN CONSOLE
            # self._render()

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # RESTART THE GAME
                if event.key == pygame.K_ESCAPE:
                    pass

                # ADD NUMBERS ON DEMAND, FOR TESTING PURPOSES
                if event.key == pygame.K_SPACE:
                    self._board.spawn_square()
                    self.print_list()

                # MOVES SQUARES UP
                if event.key == pygame.K_UP:
                    move.up(self._board)
                    self.print_list()

                # MOVE SQUARES DOWN
                if event.key == pygame.K_DOWN:
                    move.down(self._board)
                    self.print_list()

                # MOVE SQUARES LEFT
                if event.key == pygame.K_LEFT:
                    move.left(self._board)
                    self.print_list()

                # MOVE SQUARES RIGHT
                if event.key == pygame.K_RIGHT:
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
