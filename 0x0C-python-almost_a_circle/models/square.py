#!/usr/bin/python3
"""
Module with class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)
    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        """
        getter for Square's size attribute
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for Square's size attribute
        """
        self.width = value
        self.height = value
