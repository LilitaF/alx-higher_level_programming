#!/usr/bin/python3


"""Define a class"""
class Rectangle:
    """Represent a class: rectangle

    atrributes:
        number_of_instances (int) = num of rectangle instance"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialise the rectangle"""
        type(self).number_of_instances = type(self).number_of_instances + 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area

        rect_1 = must be an instance of Rectangle
        rect_2 = must be an instance of Rectangle

        Raises TypeError: if rect_1 is not an instance of rectangle
        Raises TypeError: if rect_2 is not an instance of rectangle

        return: rect_1 if both have the same area value, rect_2 if not
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """ returns a new Rectangle instance
        with width == height == size
        """

        new_rect = cls
        new_rect.width = size
        new_rect.height = size
        
        return (new_rect)

    def __str__(self):
        """ return the visual repesentation of the
        rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append(str(self.print_symbol))
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle = rectangle + ", " + str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        type(self).number_of_instances = type(self).number_of_instances - 1
        print("Bye rectangle...")
