#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        # Check if the character is lowercase and convert it to uppercase using ASCII values
        result += chr(ord(char) - (ord('a') - ord('A'))) if 'a' <= char <= 'z' else char

    print("{}".format(result))


# Example usage:
uppercase("hello")
