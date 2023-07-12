#!/usr/bin/python3
"""
Module with a class Student that defines a student
"""


class Student:
    """
    class Student that defines a student
    """
    def __int__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        """
        if type(attrs) is list and all([type(s) == str for s in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        for k, v in json.item():
            self.__dict__[k] = v
