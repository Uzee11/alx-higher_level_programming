#!/usr/bin/python3
def islower(c):
    # Check if the input is a single character and if it is lowercase
    if isinstance(c, str) and len(c) == 1 and 'a' <= c <= 'z':
        return f"{c} => lower"
    elif isinstance(c, str) and len(c) == 1 and 'A' <= c <= 'Z':
        return f"{c} => upper"
    else:
        return "Invalid input"


