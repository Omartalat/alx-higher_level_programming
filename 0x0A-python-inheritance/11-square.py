#!/usr/bin/python3
"""
Module with class Square that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Instantiation with size
        """

        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """
        return area
        """

        return self.__size * self.__size

    def __str__(self):
        """
        informal string representation of the Square
        """

        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
