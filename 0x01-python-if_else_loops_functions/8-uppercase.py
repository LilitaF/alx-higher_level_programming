#!/usr/bin/python3
def uppercase(s):
    uppercase_str = ""
    for char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert lowercase to uppercase using ASCII values
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            # If the character is already uppercase or non-alphabetic, keep it unchanged
            uppercase_char = char
        # Append the uppercase character to the result string
        uppercase_str += uppercase_char
    
    # Print the uppercase string followed by a new line
    print(uppercase_str + "\n")
