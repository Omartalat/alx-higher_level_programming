#!/usr/bin/pythoni3
"""
Module with class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        if not type(width) is int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if not type(height) is int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        if not type(x) is int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        if not type(y) is int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not type(width) is int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not type(height) is int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not type(x) is int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not type(y) is int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """
        returns the area value of the Rectangle instance.
        """
        return self.__width * self.__height

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end='')
            print("")

    def __str__(self):
        """
        overriding the __str__ method so that
        it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)
