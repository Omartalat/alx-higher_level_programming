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

    def area(size):
        """
        return area
        """

        return size * size
