#!/usr/bin/python3
"""
Module with class Base
"""
import json


class Base:
    """Base model.
    This Represents the "base" for all other classes in project 0x0C*.
    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.
        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    def to_json_string(list_dictionaries):
        """
        JSON representation of a list of dictionaries
        """
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        with open(f'{cls.__name__}.json', 'w') as json_file:
            if not list_objs:
                json_file.write("[]")
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                json_file.write(cls.to_json_string(dict_list))
    def from_json_string(json_string):
        if not json_string or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """
        Return a list of classes instantiated from a file of JSON strings.
        """
        try:
            with open(f'{cls.__name__}.json', 'r') as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
