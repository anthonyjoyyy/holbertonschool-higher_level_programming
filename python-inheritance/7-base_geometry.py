#!/usr/bin/python3
"""
This module contains an empty class
"""


class BaseGeometry:
    """class that has instance method"""

    def area(self):
        """a function that raises an exception error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value is a positive integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
