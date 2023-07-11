#!/usr/bin/python3
"""
==============================
Module with BaseGeometry class
==============================
"""


class BaseGeometry:
    """
     a class BaseGeometry with Public instance method: area
     and Public instance method: integer_validator
    """

    def area(self):
        """
        raises an Exception with the message area() is not implemented
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        validates value:
        if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
        if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
        """

        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
