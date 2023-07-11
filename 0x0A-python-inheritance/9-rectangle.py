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
        if value is not an integer: raise a TypeError exception,
        with the message <name> must be an integer
        if value is less or equal to 0: raise a ValueError exception
        with the message <name> must be greater than 0
        """

        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


"""
==============================================================
Module with a  class Rectangle that inherits from BaseGeometry
(7-base_geometry.py).
==============================================================
"""


class Rectangle(BaseGeometry):
    """
    Ractangle class inherits from Basegeometry
    """

    def __init__(self, width, height):
        """Instantiation with width and height"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", width)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """informal string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
