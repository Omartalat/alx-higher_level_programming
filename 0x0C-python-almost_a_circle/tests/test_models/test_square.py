#!/usr/bin/python3
"""
unittest for class square
"""
import unittest
from models.base import Base
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """
    TestSquareClass: unittest for class square

    """

    def test_inheritance(self):
        self.assertTrue(issubclass(Square, Base))

    def test_instantiation_size(self):
        s1 = Square(3)
        self.assertEqual(s1.size, 3)

    def test_instantiation_x(self):
        s1 = Square(3, 1)
        self.assertEqual(s1.x, 1)

    def test_instantiation_y(self):
        s1 = Square(3, 1, 5)
        self.assertEqual(s1.y, 5)

    def test_instantiation_id(self):
        s1 = Square(3, 1, 5, 10)
        self.assertEqual(s1.id, 10)

    def test__str__(self):
        s1 = Square(3, 1, 5, 10)
        self.assertEqual(str(s1), "[Square] (10) 1/5 - 3")

    def test_to_dictionary(self):
        s1 = Square(3, 1, 5, 10)
        dictionary = s1.to_dictionary()
        self.assertEqual(dictionary, {'id': 10, 'size': 3, 'x': 1, 'y': 5})
