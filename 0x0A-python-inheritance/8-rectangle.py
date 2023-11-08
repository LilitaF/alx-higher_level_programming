#!/usr/bin/python3

"""Define class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """this class inherits, represent class"""
    def __init__(self, width, height):
        """initialise Rectangle

        Args:
        - width ( +ve int): width of the rectangle(parameter)
        - height ( +ve int): height of the rectangle(parameter)

        validated by integer_validator
        integer_validator(self, name, value):
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
