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
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x,
                                                 self.y, self.width)

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

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            if kwargs:
                for k in kwargs:
                    if k == 'id':
                        self.id = kwargs[k]
                    if k == 'size':
                        self.size = kwargs[k]
                    if k == 'x':
                        self.x = kwargs[k]
                    if k == 'y':
                        self.y = kwargs[k]

    def to_dictionary(self):
        """
        returns the dictionary representation of a Square
        """
        dictionary = {}
        dictionary['id'] = self.id
        dictionary['x'] = self.x
        dictionary['size'] = self.width
        dictionary['y'] = self.y
        return dictionary
