import pygame
import config


class Renderer:
    def __init__(self, win, board):
        self._win = win
        self._board = board
        self.gridborder = pygame.Rect(
            config.BORDER_WIDTH,
            config.BOARD_Y_OFFSET,
            config.WIDTH - 2 * config.BORDER_WIDTH,
            config.WIDTH - 2 * config.BORDER_WIDTH,
        )

    def render(self):
        self._win.fill(config.BG_COLOR)
        self.game_grid()
        self.draw_squares()
        self.draw_numbers()
        pygame.display.flip()

    # DRAWING GRID FUNCTION
    def game_grid(self):
        pygame.draw.rect(
            self._win, config.GRID_COLOR, self.gridborder, width=0, border_radius=20
        )

    # FILLING SQUARES WITH COLORS AND NUMBERS
    def draw_squares(self):
        # SQUARE BACKGROUNDS
        for i in self._board.dict:
            cell_number = self._board.dict[i].get_value()
            cell_color = config.CELL_COLORS[cell_number]
            pygame.draw.rect(
                self._win,
                cell_color,
                self._board.dict[i].rect,
                width=0,
                border_radius=20,
            )

    def draw_numbers(self):
        # SQUARE NUMBERS
        for i in range(4):  # I = ROW
            for j in range(4):  # J = COL
                cell_number = self._board.dict[i * 4 + j].get_value()
                # IF CELL VALUE IS 0, NO SQUARE IS VISIBLE
                if cell_number == 0:
                    continue
                number_font = pygame.font.SysFont(
                    config.CELL_NUMBER_FONT,
                    config.CELL_NUMBER_SIZE[cell_number],
                    bold=True,
                )
                cell_number_text = number_font.render(
                    str(cell_number), 1, config.CELL_NUMBER_COLORS[cell_number]
                )
                x_coord = (
                    2 * config.BORDER_WIDTH
                    + j * (config.BORDER_WIDTH + config.SQUARE_SIZE)
                    + (config.SQUARE_SIZE // 2 - cell_number_text.get_width() // 2)
                )
                y_coord = (
                    config.BOARD_Y_OFFSET
                    + config.BORDER_WIDTH
                    + i * (config.BORDER_WIDTH + config.SQUARE_SIZE)
                    + (config.SQUARE_SIZE // 2 - cell_number_text.get_height() // 2)
                )
                self._win.blit(cell_number_text, (x_coord, y_coord))
