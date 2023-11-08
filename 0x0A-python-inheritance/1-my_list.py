#!/usr/bin/python3

"""Define class MyList """


class MyList(list):
    """represent MyList class

    inherts function lookup

    """

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)
        """
        list_sorted = sorted(self)
        print(list_sorted)
