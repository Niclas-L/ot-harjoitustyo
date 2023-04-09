import pygame
import config
from random import choice
from square import Square


class Board:
    def __init__(self):
        self.dict = {}
        self.initialize_dict()
        self.update_list()

    # INITIALIZING SELF.DICT WITH 16 SQUARE OBJECTS NUMBERED 0-15
    def initialize_dict(self):
        for i in range(16):
            x = Square(i)
            self.dict[i] = x

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

    # CHECK FOR EMPTY CELLS AND FILL ONE WITH EITHER 2 OR 4
    # CHOICE IS GIVEN AS DEFAULT VALUE FOR THE PARAMETER TO ALLOW FOR TESTING
    def spawn_square(self, new_value=0):
        # IF NO PARAMETER GIVEN, PICK A RANDOM NUMBER
        if new_value == 0:
            new_value = choice(config.NUMBER_SEED)
        empty_cell_list = []
        # GETS A LIST OF DICT KEYS FOR ALL EMPTY CELLS
        for i in self.dict:
            if self.dict[i].get_value() == 0:
                empty_cell_list.append(i)
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
