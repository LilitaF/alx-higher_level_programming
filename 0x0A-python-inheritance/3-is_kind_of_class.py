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
    curr_class = type(obj)
    while curr_class is not object:
        if curr_class is a_class:
            return (True)
        if hasattr(curr_class,'__base__'):
            curr_class = curr_class.__base__
        else:
            object
    return (False)

