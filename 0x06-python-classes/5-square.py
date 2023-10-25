#!/usri/bin/python3

"""Define a class square"""

class Square:
    """Represent the square"""
    def __init__(self, size=0):
        """Initialise the square"""
        self.__size = size

    @property
    def size(self):
        """get current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """print square with # char"""
        for i in range(0, self.__size):
            [print("#", end="") for k in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
