import unittest
import sys
import os

# Add the parent directory of the current file to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from board import Board
from square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initialize(self):
        # answer = {
        #     0: Square(0),
        #     1: Square(1),
        #     2: Square(2),
        #     3: Square(3),
        #     4: Square(4),
        #     5: Square(5),
        #     6: Square(6),
        #     7: Square(7),
        #     8: Square(8),
        #     9: Square(9),
        #     10: Square(10),
        #     11: Square(11),
        #     12: Square(12),
        #     13: Square(13),
        #     14: Square(14),
        #     15: Square(15),
        # }
        answer = {}
        for i in range(16):
            x = Square(i)
            answer[i] = x
        self.assertEqual(answer, self.board.dict)
