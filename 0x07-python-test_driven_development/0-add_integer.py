#!/usr/bin/python3

"""Define the addition function of integers"""

def add_integer(a, b=98):
    """Returns an integer: the addition of a and b

    if a and b are floats they need to be typecasted to int
    raise a TypeError exception if not float or int
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
