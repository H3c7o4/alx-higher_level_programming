#!/usr/bin/python3
"""
Module that contains the Class Base
"""
import json


class Base:
    """ Base class of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): a list of dictionnary
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): list of instances who inherits of Base
        """
        filename = type(list_objs[0]).__name__ + '.json'
        with open(filename, 'w') as f:
            if list_objs is None:
                json.dump([], f)
            elif type(list_objs[0]).__name__ == 'Rectangle':
                new_dict = [item.to_dictionary() for item in list_objs]
                json_string = cls.to_json_string(new_dict)
                json.dump(json_string, f)
