#!/usr/bin/python3
"""
==============================
Module with function read_file
==============================
"""


def read_file(filename=""):
    with open(f'{filename}', 'r', encoding="utf-8") as f:
        print(f.read(), end='')
