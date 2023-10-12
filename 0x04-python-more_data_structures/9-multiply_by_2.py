#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    multiplied_dic = {}

    for key, value in a_dictionary.items():
        multiplied_value = value * 2
        multiplied_dic[key] = multiplied_value

    return (multiplied_dic)
