#!/usr/bin/python3
"""
This module contains a Square class and defines a square
"""


class Square:
    """
    This class defines a square.
    """
    def __init__(self, size=0):

        self.size = size

        @property
        def size(self):
            return self.__size

        @size.setter
        def size(self, value):
            if type(value) is not int:
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
