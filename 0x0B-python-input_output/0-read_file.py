#!/usr/bin/python3
"""
==============================
Module with function read_file
==============================
"""


def read_file(filename=""):
    """
    a function that reads a text file (UTF8) and prints it to stdout
    """

    with open(f'{filename}', encoding="utf-8") as f:
        print(f.read(), end='')
