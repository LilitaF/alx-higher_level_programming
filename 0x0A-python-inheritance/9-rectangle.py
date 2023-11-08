#!/usr/bin/python3

""" Define class Rectangle that inherits frm BaseGeometry"""


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

    def area(self):
        """Returns area of the Rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Return the print() and str() representation of a Rectangle"""
        descr = "[" + str(self.__class__.__name__) + "] "
        descr = descr + str(self.__width) + "/" + str(self.__height)
        return (descr)
