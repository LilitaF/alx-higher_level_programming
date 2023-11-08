#!/usr/bin/python3

"""Lookup function"""


def lookup(obj):
    """
    Returns the list of available attributes
    and methods of an object

    args:
    any Python object

    Returns: List of available attributes and methods
    """

    return dir(obj)
