#!/usr/bin/python3
output = ''
for letter in range(97, 123):
    if chr(letter) not in ['q', 'e']:
        output += '{}'.format(chr(letter))

print(output, end='')
