#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list_storage = []

    for digit in my_list:
        if digit % 2 == 0:
            list_storage.append(True)
        else:
            list_storage.append(False)

    return (list_storage)
