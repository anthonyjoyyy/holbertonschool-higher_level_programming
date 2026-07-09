#!/usr/bin/python3

"""
This module contains a function that prints the square of a number.
"""


def print_square(size):
    if type(size) not in [int]:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) in [float] and size < 0:
        raise TypeError("size must be an integer")
