#!/usr/bin/python3
"""
========================
Module with class Mylist
========================
"""


class MyList(list):
    """
    class with method print_sorted
    """
    pass

    def print_sorted(self):
        """
        function:
        prints the list, but sorted (ascending sort)
        """

        print(sorted(list(self)))
