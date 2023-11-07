#!/usr/bin/python3

"""Define class Square that inherits frm Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represent Square"""

    def __init__(self, size):
        """Initialise the class

        Args:
        - size ( +ve int): must be private
        validated by integer_validator

        def integer_validator(self, name, value):
        """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
