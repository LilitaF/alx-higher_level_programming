#!/usr/bin/python3
def pow(a, b):
    # Base case: when exponent is 0, result is 1
    if b == 0:
        return 1

    # If exponent is negative, compute reciprocal of the number raised to positive exponent
    if b < 0:
        a = 1 / a
        b = abs(b)

    result = 1
    # Multiply the base 'a' 'b' times to calculate a^b
    for _ in range(b):
        result *= a

    return (result)
