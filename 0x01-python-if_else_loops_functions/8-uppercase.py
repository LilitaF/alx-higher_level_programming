#!/usr/bin/python3
def uppercase(str):
    formatted_string = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            uppercase_char = chr(ord(char) - 32)
        else:
            char
        formatted_string += "{}".format(uppercase_char)
    print(formatted_string)
