#!/usr/bin/python3
"""
==================================
Module with inherits_from Function
==================================
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class;
    otherwise False.
    """

    obj_classes = type(obj).__mro__
    for cls in obj_classes:
        if cls is a_class:
            continue
        if issubclass(cls, a_class):
            return True
    return False
