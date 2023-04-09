import unittest
import sys
import os

# Add the parent directory of the current file to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # nopep8
from square import Square  # nopep8


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square = Square(0)

    def test_repr(self):
        self.assertTrue(str(self.square) == "0")

    def test_get_value(self):
        answer = self.square.get_value()
        self.assertEqual(answer, 0)

    def test_set_value(self):
        self.square.set_value(16)
        self.assertEqual(16, self.square.get_value())

    def test_grow(self):
        self.square.set_value(2)
        self.square.grow()
        self.assertEqual(4, self.square.get_value())

    def test_reset(self):
        self.square.set_value(16)
        self.square.reset()
        self.assertEqual(0, self.square.get_value())
