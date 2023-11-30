#!/usr/bin/python3
def print_last_digit(number):
    try:
        last_digit = abs(int(number)) % 10
        print(f"{last_digit:02d}")
        return last_digit
    except ValueError:
        print("Invalid input: not a number")

# Example usage:
result = print_last_digit("Holberton")
print(result)

