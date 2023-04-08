import pygame
import config
import move

fps = config.FPS


class GameLoop:
    def __init__(self, clock, event_queue, renderer, board):
        self._clock = clock
        self._event_queue = event_queue
        self._renderer = renderer
        self._board = board
        self.print_list()

    def start(self):
        # GAME STARTS WITH TWO SQUARES FILLED ALREADY
        self._board.spawn_square()
        self._board.spawn_square()

        while True:
            self._clock.tick(fps)
            self._handle_events()

            # NOT BOTHERING WITH GRAPHICS UNTIL CORE GAME LOOP WORKS IN CONSOLE
            # self._render()

    def _handle_events(self):
        self.keys_pressed = pygame.key.get_pressed()
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                exit()

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
        for i in self._board.list:
            print(i)
        print()
