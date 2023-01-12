#!/usr/bin/python3
"""
Module that contain a class Rectangle


Class that inherit from Base
"""
from models.base import Base


class Rectangle(Base):
    """Class that defines a rectangle"""
    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Retrieves the value of the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the necessary attributes for the Rectangle object.
        Args:
            width (int): the width of the square.
        Raises:
            TypeError: if width is not given as an integer.
            ValueError: if width is less than 0.
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the value of the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the necessary attributes for the Rectangle object.
        Args:
            height (int): the height of the square.
        Raises:
            TypeError: if width is not given as an integer.
            ValueError: if height is less than 0.
        """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Retrieves the value of x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Sets the necessary attributes for the Rectangle object.
        Args:
            x (int): the width of the square.
        Raises:
            TypeError: if width is not given as an integer.
            ValueError: if width is less than 0.
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        else:
            self.__x = value

    @property
    def y(self):
        """Retrieves the value of x"""
        return (self.__y)

    @x.setter
    def y(self, value):
        """Sets the necessary attributes for the Rectangle object.
        Args:
            x (int): the width of the square.
        Raises:
            TypeError: if width is not given as an integer.
            ValueError: if width is less than 0.
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        else:
            self.__y = value
