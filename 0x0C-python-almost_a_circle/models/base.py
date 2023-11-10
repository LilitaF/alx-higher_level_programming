#!/usr/bin/python3

""" Define class Base"""


class Base:
    """Represent class Base

    This is the base for all other classes in this project:
    Almost a circle

    Attributes:
        __nb_objects: private, nr of objects instantiated
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialise class 

        Args:
        - id (int): new base's id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
