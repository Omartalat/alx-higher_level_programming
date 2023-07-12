#!/usr/bin/python3
"""
Module with class MyInt that inherits from int
"""


class MyInt(int):
    """
    class MyInt that inherits from int
    """

    def __eq__(self, other):
        """
        inverted ==
        """
        return not int.__eq__(self, other)

    def __ne__(self, other):
        """
        inverted !=
        """
        return not int.__ne__(self, other)
