#!/usr/bin/python3
"""
defines unittest for rectangle.py
"""
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Rectangle class.
    """
    def test_inheritance(self):
        self.assertTrue(issubclass(Rectangle, Base))