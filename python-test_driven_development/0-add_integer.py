#!/usr/bin/python3

"""
This module provides a function where two integers are added together.
"""


def add_integer(a, b=98):
    """
    It ensures that the inputs are valid numbers before adding them.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
