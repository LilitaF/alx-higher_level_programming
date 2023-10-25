#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert lowercase to uppercase using ASCII values and format the result
            uppercase_char = '{}'.format(chr(ord(char) - ord('a') + ord('A')))
        else:
            # If the character is already uppercase or non-alphabetic, keep it unchanged
            uppercase_char = char
        # Append the formatted uppercase character to the result string
        uppercase_str += uppercase_char
    
    # Print the formatted uppercase string followed by a new line
    print('{}\n'.format(uppercase_str))
