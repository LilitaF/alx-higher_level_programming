#!/usr/bin/python3

"""Define function: is_kind_of_class"""
def is_kind_of_class(obj, a_class):
    """Represent funtion

    Args:
    - obj: object to determine if it was inherited
    from a class or if it is just an instance, or not
    - a_class: class searched

    Return:
    True if the object is an instance of, or if the
    object is an instance of a class that
    inherited from, the specified class; otherwise False
    """
    if isinstance(obj, a_class):
        return (True)
    return (False)

