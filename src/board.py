from random import choice

import config
from square import Square


class Board:
    def __init__(self):
        self.dict = {}
        self.initialize_dict()
        self.update_list()
        self.score = 0

    # INITIALIZING SELF.DICT WITH 16 SQUARE OBJECTS NUMBERED 0-15
    # AS WELL AS PYGAME RECT OBJECTS FOR EACH SQUARE
    def initialize_dict(self):
        # # CREATING PYGAME RECT OBJECTS FOR EACH SQUARE OBJECT IN BOARD.DICT
        for i in range(4):
            for j in range(4):
                x_coord = 2 * config.BORDER_WIDTH + j * (
                    config.BORDER_WIDTH + config.SQUARE_SIZE
                )
                y_coord = (
                    config.BOARD_Y_OFFSET
                    + config.BORDER_WIDTH
                    + i * (config.BORDER_WIDTH + config.SQUARE_SIZE)
                )
                k = Square(i * 4 + j, x_coord, y_coord)
                self.dict[i * 4 + j] = k

    # CREATES A 4 X 4 MATRIX FROM THE VALUES OF THE SQUARE OBJECTS IN SELF.DICT
    def update_list(self):
        self.list = [
            [
                self.dict[0].get_value(),
                self.dict[1].get_value(),
                self.dict[2].get_value(),
                self.dict[3].get_value(),
            ],
            [
                self.dict[4].get_value(),
                self.dict[5].get_value(),
                self.dict[6].get_value(),
                self.dict[7].get_value(),
            ],
            [
                self.dict[8].get_value(),
                self.dict[9].get_value(),
                self.dict[10].get_value(),
                self.dict[11].get_value(),
            ],
            [
                self.dict[12].get_value(),
                self.dict[13].get_value(),
                self.dict[14].get_value(),
                self.dict[15].get_value(),
            ],
        ]
        self.update_score()

    # UPDATES THE SCORE
    def update_score(self):
        # RESETS THE SCORE, THEN ADDS THE VALUE OF EACH SQUARE TO IT
        self.score = 0
        for i in self.dict.items():
            self.score += i[1].get_value()

    # CHECK FOR EMPTY CELLS AND FILL ONE WITH EITHER 2 OR 4
    # CHOICE IS GIVEN AS DEFAULT VALUE FOR THE PARAMETER TO ALLOW FOR TESTING
    def spawn_square(self, new_value=0):
        # IF NO PARAMETER GIVEN, PICK A RANDOM NUMBER
        if new_value == 0:
            new_value = choice(config.NUMBER_SEED)
        empty_cell_list = []
        # GETS A LIST OF DICT KEYS FOR ALL EMPTY CELLS
        # .ITEMS() RETURNS A LIST OF TUPLES, SO WE NEED TO ACCESS THE SECOND ELEMENT OF EACH TUPLE
        for i in self.dict.items():
            if i[1].get_value() == 0:
                empty_cell_list.append(i[0])
        # PICKS A RANDOM EMPTY CELL AND CALLS IT'S SET_VALUE METHOD
        if empty_cell_list:
            new_cell = choice(empty_cell_list)
            self.dict[new_cell].set_value(new_value)
        self.update_list()

    def merge_squares(self, i, j):
        # IF SAME NUMBERS, MERGE AND RESET
        if self.dict[i].get_value() == self.dict[j].get_value():
            self.dict[j].grow()
            self.dict[i].reset()

    def reset(self):
        for i in self.dict:  # pylint: disable=consider-using-dict-items
            self.dict[i].reset()
        self.spawn_square()
        self.spawn_square()
