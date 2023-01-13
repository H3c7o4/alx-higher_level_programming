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
        return json.dumps(list_dictionaries)
