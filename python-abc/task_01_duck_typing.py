#!/usr/bin/python3
"""
creating a module where we create a circle learn more about duck typing.
"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """return area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """return perimeter of the shape"""
        pass


class Circle(Shape):
    """Circle class"""

    def __init__(self, radius):
        """initialising circle"""
        self.radius = radius

    def area(self):
        """returning circle area"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """"returning perimeter of circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class"""

    def __init__(self, width, height):
        """initialising rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """returning rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """returning perimeter of rectangle"""
        return (2 * self.width) + (2 * self.height)

def shape_info(shape):
    """prints area and perimeter of shape"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
