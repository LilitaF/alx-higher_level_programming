#!/usr/bin/python3
from models.rectangle import Rectangle

"""Define the class Square that inherits from rectangle"""
class Square(Rectangle):
    """Represent the class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialise the class Square

        Args:
        - size: value assigned as width and height
        - x: coordinates of new square
        - y: coordinates of new square
        - id: identity of new square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for the size of the square"""
        return self.height

    @size.setter
    def size(self, value):
        """setter for the size of the square"""
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """update the square and assigns attributes

        Args:
        - 1st argument should be the id attribute
        - 2nd argument should be the size attribute
        - 3rd argument should be the x attribute
        - 4th argument should be the y attribute

        **kwargs must be skipped if *args exists
        and is not empty

        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        elif kwargs:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v


    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {"id":  self.id,
                "size": self.height,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """returns str() and print() representation of square"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.height))
