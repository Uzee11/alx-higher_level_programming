#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1

    print("{} argument{}:".format(num_args, 's' if num_args != 1 else ''), end='')

    if num_args == 0:
        print(".")

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("\n{}: {}".format(i, arg))
