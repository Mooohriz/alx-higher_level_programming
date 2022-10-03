#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_(unittest.TestCase):
    """Define unittests for square"""
    def test_square_with_no_args(self):
        """testing with no argument in square()"""
        with self.assertRaises(TypeError):
            print(Square())

    def test_square_with_one_arg(self):
        """testing with one argument"""
        sq = Square(13)
        self.assertEqual(str(sq), "[Square] (1) 0/0- 13)")

    def test_rectangle_with_three_args(self):
        """Test with two arguments"""
        sq = Square(13, 1)
        self.assertEqual(str(sq), "[Square] (1) 1/0- 13)")

    def test_rectangle_with_four_args(self):
        """Test with three arguments"""
        sq = Square(13, 1, 3)
        self.assertEqual(str(sq), "[Square] (1) 1/3- 13)")

    def test_with_five_args(self):
        """Test with five arguments"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        self.assertEqual(rec1.id, 2)