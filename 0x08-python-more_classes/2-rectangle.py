#!/usr/bin/python3
"""
Class Rectangle: Defines a rectangle based on 1-rectangle.py
"""


class Rectangle:
    """class that defines a rectangle with his attributes"""
    def __init__(self, width=0, height=0):
        """Initialize attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the value of the width"""
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
        if (value is not int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            return self.__width = value

    @property
    def height(self):
        """Get the value of the height"""
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
        if (value is not int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            return (self.__height = value)

    def area(self):
        """Retrieves the area of the Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Retrieves the perimeter of the Rectangle"""
        if (self.__width == 0) or (self.__height == 0):
            return 0
        return (self.__width + self.__height) * 2