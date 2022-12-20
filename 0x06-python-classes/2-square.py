#!/usr/bin/python3
"""
Class Square: Create a square class that contains a size
"""

class Square:
    """ Class that defines a square with size"""
    def __init__(self, size=0):
        try:
            if size >= 0:
                self.__size = size
        except ValueError:
            print("size must be >= 0")
