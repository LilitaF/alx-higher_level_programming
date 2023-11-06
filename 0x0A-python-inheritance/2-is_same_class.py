#!/usr/bin/python3

"""Define function: is_same_class"""
def is_same_class(obj, a_class):
    """True or False function

    Args:
    - obj: is exactly an instance of the specified class
    - a_class: specified class to look for the instance

    Return:
    True if the object is exactly an instance
    of the specified class; otherwise False.
    """
    return (type(obj) == a_class)

