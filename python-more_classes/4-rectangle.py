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
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0

        return (self.width * 2) + (self.height * 2)

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

    def __str__(self):
        """Returns an informal and nicely printable string representation of
        the rectangle using the # character.
        """
        if self.width == 0 or self.height == 0:
            return ""

        rectangle = []

        for i in range(self.__height):
            rectangle.append("#" * self.__width)

        return "\n".join(rectangle)

    def __repr__(self):
        """Returns a string representation to recreate the object."""
        return "Rectangle({}, {})".format(self.__width,self.__height)
