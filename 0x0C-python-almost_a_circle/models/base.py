#!/usr/bin/python3
"""
Module that contains the Class Base
"""


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
