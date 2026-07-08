#!/usr/bin/python3

"""
This module provides a function where two integers are added together.
"""


def add_integer(a, b=98):
    """
    It ensures that the inputs are valid numbers before adding them.
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return a + b
