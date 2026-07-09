#!/usr/bin/python3

"""
This module contains a function that prints the square of a number.
"""


def print_square(size):

    """
prints a square with the character '#'
"""

    if type(size) not in [int]:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        print("#" * size)
