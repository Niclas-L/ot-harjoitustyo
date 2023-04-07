import pygame
import config
from random import choice
from sprites.square import Square

class Board:
    def __init__(self):
        self.dict = {
            0:0, 1:0, 2:0, 3:0, 
            4:0, 5:0, 6:0, 7:0, 
            8:0, 9:0, 10:0, 11:0, 
            12:0, 13:0, 14:0, 15:0
            }
        # GAME STARTS WITH TWO SQUARES ALREADY FILLED
        self.spawn_square()
        self.spawn_square()
        self.update_list()
    
    def update_list(self):
        self.list = [
            [self.dict[0], self.dict[1], self.dict[2], self.dict[3]],
            [self.dict[4], self.dict[5], self.dict[6], self.dict[7]],
            [self.dict[8], self.dict[9], self.dict[10], self.dict[11]],
            [self.dict[12], self.dict[13], self.dict[14], self.dict[15]]
        ]
    
    # CHECK FOR EMPTY CELLS AND FILL ONE WITH EITHER 2 OR 4
    def spawn_square(self):
        # WAITS A SHORT WHILE BEFORE SPAWNING NEW NUMBER, MAKES IT EASIER TO GRASP WHERE THE NEW NUMBER SPAWNS
        pygame.time.wait(config.DELAY)
        empty_cell_list = []
        # GETS A LIST OF DICT KEYS FOR ALL EMPTY CELLS
        for i in self.dict:
            if self.dict[i] == 0:
                empty_cell_list.append(i)
        # PICKS A RANDOM EMPTY CELL AND FILLS IT WITH EITHER 2 OR 4
        if empty_cell_list:
            new_cell = choice(empty_cell_list)
            self.dict[new_cell] = choice((2, 4))
        self.update_list()