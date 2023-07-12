#!/usr/bin/python3
"""
Module with append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(f'{filename}', 'r') as f:
        text = f.readlines()
    with open(f'{filename}', 'w') as fi:
        new_text = ""
        for line in text:
            new_text += line
            if search_string in line:
                new_text += new_string
        fi.write(new_text)
