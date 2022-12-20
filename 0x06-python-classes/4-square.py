#!/usr/bin/python3
"""
Square class: defines a square
"""


class Square:
    """class Square that defines a squaare"""
    def __init__(self, size):
        """Sets the necessary attributes for the Square object.
        Args:
            size (int): the size of one edge of the square.
        Raises:
            TypeError: if size is not given as an integer.
            ValueError: if size is less than 0.
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def area(self):
        """Return the area of the square"""
        return (self.__size * self.__size)
    
    @property.setter
    def size(self, value):
        """Set the value of size"""
        self.__size = value
