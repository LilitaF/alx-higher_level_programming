#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        # Try to format the value as an integer and print it
        formatted_value = "{:d}".format(value)
        print(formatted_value)
        return (True)
    except (ValueError, TypeError):
        # If an error occurs, print the error message to stderr
        print("Exception: Invalid input", file=sys.stderr)
        return (False)
