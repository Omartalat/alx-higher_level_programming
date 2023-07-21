#!/usr/bin/python3
"""
Module with class Rectangle
"""


class Rectangle:
    """
    class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Instantiation
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """
        returns the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            rect_perimeter = 0
        else:
            rect_perimeter = 2 * (self.__width + self.__height)
        return rect_perimeter

    def __str__(self):

        rect_str = ""
        if self.__width == 0 or self.__height == 0:
            return rect_str
        for i in range(self.__height):
            for j in range(self.__width):
                rect_str += "#"
            rect_str += "\n"
        return rect_str[:-1]
