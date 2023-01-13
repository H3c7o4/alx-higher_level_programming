#!/usr/bin/python3
"""
Module based on class Rectangle


Contains a class called Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class inherits from Rectangle and defines a square object

    Attributes:
        size (int): The width of the square
        x (int): The horizontal (x) padding of the square
        y (int): The vertical (y) padding of the square
        id (int): The identification of the object
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square object

           Args:
                size (int): The width of the square
                x (int): The horizontal (x) padding of the square
                y (int): The vertical (y) padding of the square
                id (int): The identification of the square object
        """
        super().__init__(size, size, x, y, id)

        def __str__(self):
            """Overrides the default behaviour of the __str__ method."""
            return "[Rectangle] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)
