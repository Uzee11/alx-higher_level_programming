#!/usr/bin/python3
def islower(c):
    # Check if the input is a single character and if it is lowercase
    if len(c) == 1 and 'a' <= c <= 'z':
        return f"{c} => lower"
    else:
        return f"{c} => not lower"

# Example usage:
character = 'a'
result = islower(character)
print(result)  # This should print 'a => lower'
