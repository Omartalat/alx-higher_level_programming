#!/usr/bin/python3
"""
=================================
Module with a function write_file
=================================
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8)
    and returns the number of characters written:
    """

    with open(f'{filename}', 'w', encoding='utf-8') as f:
        return f.write(text)
