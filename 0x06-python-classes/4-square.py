#!/usr/bin/python3
"""Define a square"""
class Square:
    """Represent the square"""
    def __init__(self, size=0):
        """Initialise the square"""
        self.__size = size

    @property
    def size(self):
        """to retrieve size of the square"""
        return (self.__size)
    @size.setter
    def size(self, value):
        """to set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)
