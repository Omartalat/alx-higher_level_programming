#!/usr/bin/python3
"""
defines unittest for rectangle.py
"""
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """
    Unittests for testing instantiation of the Rectangle class.
    """

    def test_inheritance(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_instantiation_type_width(self):
        with self.assertRaises(TypeError):
            Rectangle("Omar", 12, 23, 34)

    def test_instantiation_type_height(self):
        with self.assertRaises(TypeError):
            Rectangle(12, "Talat", 23, 34)

    def test_instantiation_type_x(self):
        with self.assertRaises(TypeError):
            Rectangle(12, 23, "Talat", 34)

    def test_instantiation_type_y(self):
        with self.assertRaises(TypeError):
            Rectangle(12, 23, 23, "Talat")

    def test_instantiation_value_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 12, 23, 34)

    def test_instantiation_value_height(self):
        with self.assertRaises(ValueError):
            Rectangle(12, 0, 23, 34)

    def test_instantiation_value_x(self):
        with self.assertRaises(ValueError):
            Rectangle(12, 23, -1, 34)

    def test_instantiation_value_y(self):
        with self.assertRaises(ValueError):
            Rectangle(12, 23, 23, -1)

    def test_width_getter_setter(self):
        r1 = Rectangle(21, 123, 34, 45)
        self.assertEqual(r1.width, 21)

    def test_height_getter_setter(self):
        r1 = Rectangle(21, 123, 34, 45)
        self.assertEqual(r1.height, 123)

    def test_height_getter_setter(self):
        r1 = Rectangle(21, 123, 34, 45)
        self.assertEqual(r1.x, 34)

    def test_height_getter_setter(self):
        r1 = Rectangle(21, 123, 34, 45)
        self.assertEqual(r1.y, 45)

    def test_area(self):
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.area(), 6)

    def test__str__(self):
        r1 = Rectangle(5, 6, 4, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 4/1 - 5/6")

    def test_update_arg(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(100, 2, 3, 4, 5)
        self.assertEqual(str(r1), '[Rectangle] (100) 4/5 - 2/3')

    def test_update_kwarg(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=3, width=89, x=4, y=5, id=20)
        self.assertEqual(str(r1), '[Rectangle] (20) 4/5 - 89/3')

    def test_to_dictionary(self):
        rect = Rectangle(20, 12, 3, 5, 6)
        r1_dictionary = rect.to_dictionary()
        self.assertEqual(
            r1_dictionary, {'x': 3, 'y': 5, 'id': 6, 'height': 12,
                            'width': 20})
