#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_ints = {}

    for num in my_list:
        unique_ints[num] = True

    sum_of_unique_ints = sum(unique_ints)

    return (sum_of_unique_ints)
