#!/usr/bin/python3
"""
Square class: defines a square
"""


class Square:
    """class Square that defines a squaare"""
    def __init__(self, size=0):
        """Initialize attributes"""
        self.size = size

    @property
    def size(self):
        """Return the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the necessary attributes for the Square object.
        Args:
            size (int): the size of one edge of the square.
        Raises:
            TypeError: if size is not given as an integer.
            ValueError: if size is less than 0.
        """
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """ retrieve the initial potition """
        return self.__position

    @position.setter
    def position(self, value):
        """ sets the new position """
        s = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple:
            raise TypeError(s)
        elif (len(value) != 2):
                raise TypeError(s)
        else:
            for t in value:
                if (t < 0):
                    raise TypeError(s)
                elif (type(t) is not int):
                    raise TypeError(S)
        self.__position = value

    def area(self):
        """Return the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """that prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for n in range(self.__position[1]):
                print("")
            for x in range(self.__size):
                for y in range(self.__size + self.__position[0]):
                    if (y < self.__position[0]):
                        print(" ", end="")
                    else:
                        print("#", end='')
                print('')
