#!/usr/bin/python3
def uppercase(s):
    for char in s:
        # Check if the character is lowercase and convert it to uppercase
        print(chr(ord(char) - 32) if 'a' <= char <= 'z' else char, end='')
    print()  # Print a new line after the loop
