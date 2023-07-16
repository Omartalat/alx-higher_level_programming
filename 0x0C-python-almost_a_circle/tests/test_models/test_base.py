#!/usr/bin/python3
"""
Defines unittests for base.py
"""
import unittest


class TestBaseInstantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Base class.
    """
    def test_id_none(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_none_2(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id -2)
    
class TestRectangleInstantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Rectangle class.
    """

