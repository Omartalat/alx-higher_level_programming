#!/usr/bin/python3
"""
Defines a class Student.
"""


class Student:
    """
    Represent a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        """

        if attrs is None:
            return self.__dict__
        if type(attrs) is list:
            all_str = True
            for el in attrs:
                if not isinstance(el, str):
                    all_str = False
            if all_str:
                json_dict = {}
                for attr in attrs:
                    if hasattr(self, attr):
                        json_dict[attr] = getattr(self, attr)
                return json_dict
