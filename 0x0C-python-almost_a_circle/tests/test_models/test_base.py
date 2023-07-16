#!/usr/bin/python3
"""
Defines unittests for base.py
"""
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """
    Unittests for testing Base class.
    """

    def test_id_none(self):
        """
        Unittests for testing instantiation of the Base class.
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b1.id, b3.id - 2)
        self.assertEqual(b2.id, b3.id - 1)

    def test_to_json_string(self):
        """
        Unittests for testing to_json_string() method of the Base class.
        """
        b1 = Base.to_json_string([])
        self.assertEqual(b1, "[]")

    def test_file_rectangle(self):
        """
        Test check if file loads from rectangle
        """
        R1 = Rectangle(33, 34, 35, 26)
        R2 = Rectangle(202, 2)
        lR = [R1, R2]
        Rectangle.save_to_file(lR)
        lR2 = Rectangle.load_from_file()
        self.assertNotEqual(lR, lR2)

    def test_file_square(self):
        """
        Test check if file loads from square
        """
        S1 = Square(22)
        S2 = Square(44, 44, 55, 66)
        lS = [S1, S2]
        Square.save_to_file(lS)
        lS2 = Square.load_from_file()
        self.assertNotEqual(lS, lS2)

    def test_from_json_string(self):
        """
        Test check from json string
        """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        with self.subTest():
            r1 = Rectangle(10, 7, 2, 8, 1)
            r1_dict = r1.to_dictionary()
            json_dict = Base.to_json_string([r1_dict])
            self.assertEqual(r1_dict, {'x': 2, 'width': 10,
                                       'id': 1, 'height': 7,
                                       'y': 8})
            self.assertIs(type(r1_dict), dict)
            self.assertIs(type(json_dict), str)
            self.assertEqual(json.loads(json_dict), json.loads('[{"x": 2, '
                                                               '"width": 10, '
                                                               '"id": 1, '
                                                               '"height": 7, '
                                                               '"y": 8}]'))
