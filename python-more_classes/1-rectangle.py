#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""


class Rectangle:
    """
    defining a rectangle
    """
    def __init__(self, width=0, height=0):

        self.__width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if height < 0:
                raise ValueError("height must be >= 0")
