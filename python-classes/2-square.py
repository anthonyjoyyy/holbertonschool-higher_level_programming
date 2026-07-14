#!/usr/bin/python3
"""
This module contains a Square class and defines a square
"""


class Square:
    """
    This class defines a square, now raising exception messages.
    """
    def __init__(slef, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        slef.__size = size
