#!/usr/bin/python3

"""Defining a class"""
class Rectangle:
    """Represent class: rectangle"""
    def __init__(self, width=0, height=0):
        """Initialise class: rectangle

        args:
            width(int): width of a rectangle
            height(int): height of a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width: width is private"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get value of height: height is private"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

