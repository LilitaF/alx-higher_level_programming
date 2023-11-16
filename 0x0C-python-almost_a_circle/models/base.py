#!/usr/bin/python3

""" Define class Base"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries

        Args:
        - list_dictionaries: list of dictionaries
        If is None or empty, return the string: "[]"
        """
        if list_dictionaries is None or list_dictionaries is {}:
            return ([])
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation
        of list_objs to a file.

        Args:
        - cls: class
        - list_objs: list of instances who inherits of Base
        e.g Rectangle instances

        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                dictionaries = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON
        string representation json_string
        Return the deserialization of a JSON string.

        Args:
        - json_string: is a JSON string representing
        a list of dictionaries

        Return:
        - If json_string is None or empty, return an empty list
        - Otherwise, return the list represented by json_string

        """
        if json_string is None or json_string == "[]":
            return ([])
        return (json.loads(json_string))
