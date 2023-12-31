#!/usr/bin/python3

"""Define the square"""

class Square:
    """Represent the square"""
    def __init__(self, size=0):
        """initialise the square

        Args:
            size(int): Size of square must be int.
            """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the are of a square"""
        return (self.__size * self.__size)
