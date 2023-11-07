#!/usr/bin/python3

"""Define class: BaseGeometry"""
class BaseGeometry:
    """Represent BaseGeometry"""
    def area(self):
        """area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function validates the value

        Args:
        - name: is always a string, name of parameter
        - value: parameter to validate, int

        Raises:
        - TypeError: if value is not integer
        - ValueError: if value <= 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

