#!/usr/bin/python3
"""Module built for Python 0x07 task 0.
"""


def add_integer(a, b=98):
    """Function that adds two integers.

    Args:
        a ((int, (float)): first arg to add to sum.
        b ((int, (float)): second arg to add to sum. Defaults to 98.

    Returns: sum of both values.

    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
