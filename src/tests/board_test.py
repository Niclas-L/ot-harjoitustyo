import unittest
import sys
import os

# Add the parent directory of the current file to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import config
from board import Board
from square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    # TESTS IF BOARD.INITIALIZE() CREATES A DICTIONARY WITH 16 SQUARE OBJECTS AS VALUES
    def test_initialize(self):
        l = []
        for i in range(16):
            x = Square(i)
            if type(x) == type(self.board.dict[i]):
                l.append(i)
        self.assertEqual(16, len(l))

    # TESTS IF BOARD IS INITIALIZED WITH A CORRECTLY STRUCTURED BOARD.LIST
    def test_update_list(self):
        answer = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(answer, self.board.list)

    # TESTING IF NEW VALUE IS ADDED TO BOARD CORRECTLY
    def test_spawn_square(self):
        self.board.spawn_square(8)
        answer = False
        for i in self.board.dict:
            if self.board.dict[i].get_value() == 8:
                answer = True
        self.assertTrue(answer)

    def test_spawn_square_not_empty(self):
        for i in range(5):
            self.board.spawn_square(2)
        self.board.spawn_square(8)
        answer = False
        for i in self.board.dict:
            if self.board.dict[i].get_value() == 8:
                answer = True
        self.assertTrue(answer)
    
    def test_spawn_square_already_full(self):
        for i in range(16):
            self.board.spawn_square(2)
        self.board.spawn_square(8)
        answer = False
        for i in self.board.dict:
            if self.board.dict[i].get_value() == 8:
                answer = True
        self.assertFalse(answer)

    def test_spawn_square_default(self):
        self.board.spawn_square()
        answer = False
        for i in self.board.dict:
            if self.board.dict[i].get_value() in config.NUMBER_SEED:
                answer = True
        self.assertTrue(answer)

    # TESTING IF MERGING SQUARES HANDLES VALUE GROWTH AND RESET CORRECTLY
    def test_merge_squares(self):
        self.board.dict[0].set_value(2)
        self.board.dict[1].set_value(2)
        self.board.merge_squares(0, 1)
        self.assertEqual((0, 4), (self.board.dict[0].get_value(), self.board.dict[1].get_value()))

    def test_merge_squares_not_identical(self):
        self.board.dict[0].set_value(2)
        self.board.dict[1].set_value(4)
        self.board.merge_squares(0, 1)
        self.assertEqual((2, 4), (self.board.dict[0].get_value(), self.board.dict[1].get_value()))
