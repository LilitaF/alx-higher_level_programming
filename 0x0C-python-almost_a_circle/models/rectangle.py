#!/usr/bin/python3
"""Define class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Represent class Rectangle

    Attributes:
    - __width (private): own public getter and setter
    - __height (private): own public getter and setter
    - __x (private): own public getter and setter
    - __y (private): own public getter and setter

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialies the rectangle

        Args:
        - __width: width of new rectangle
        - __height: height of new rectangle
        - x: coordinate for rectangle
        - y: coordinate for rectangle
        - id: identity for new rectangle

        Raises:
        - TypeError: if width, height, x and y are not integers
        - ValueError: if width and height are <= 0
        - ValueError: if x and y < 0

        """
        self.__width = width
        self.__height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter of rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """width setter of rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter of rectangle"""
        return (self.__width)

    @height.setter
    def height(self, value):
        """height setter of rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter of rectangle"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """ x setter of rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter of rectangle"""
        return(self.__y)

    @y.setter
    def y(self, value):
        """y setter of rectangle"""
        if type(value) is not int:
            raise TypeError("y must be integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    def area(self):
        """return the area value of the Rectangle instance."""
        return (self.__width * self.__height)

    def display(self):
        """Represent rectangle by print #
        as a display for the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            print("")
            return

        for d in range(self.__y):
            print("")


        for a in range(self.__height):
            for c in range(self.__x):
                print(" ", end="")
            for b in range(self.__width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """assigns arguments to each attributes
        update rectangle

        Args:
        --*args: new int values

        - 1st argument: represents id attribute
        - 2nd argument: represents width attribute
        - 3rd argument: represents height atttribute
        - 4th argument: represents x attribute
        - 5th argument: represents y attribute

        """

        if args:
            if len(args) >= 1:
                self.id = args[0]

            if len(args) >= 2:
                self.__width = args[1]

            if len(args) >= 3:
                self.__height = args[2]

            if len(args) >= 4:
                self.__x = args[3]

            if len(args) >= 5:
                self.__y = args[4]
        else:
            pass

        for k, v in kwargs.items():
            if k == "id":
                self.id = v
            elif k == "width":
                self.__width = v
            elif k == "height":
                self.__height = v
            elif k == "x":
                self.__x = v
            elif k == "y":
                self.__y = v


    def __str__(self):
        """Return the print() and str() representation of the Rectangle
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
            self.__x, self.__y, self.__width, self.__height))
