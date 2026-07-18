#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""


class Rectangle:
    """
    defining a rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance."""

        self.width = width
        self.height = height

    def area(self):
        return self.width * selfheight

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0

        return (width * 2) + (height * 2)

    @property
    def width(self):
        """Getter: Retrieves the private __width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter: Validates and sets the private __width attribute."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")

            self.__width = value

    @property
    def height(self):
        """Getter: Retrieves the private __height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter: Validates and sets the private __height attribute."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")

            self.__height = value
