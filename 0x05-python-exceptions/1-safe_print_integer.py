#!/usr/bin/python3
def safe_print_integer(value):
    try:
        needed_format = "{:d}".format(value)

        print(needed_format)
        return (True)
    except (ValueError, TypeError):
        pass
        return (False)
