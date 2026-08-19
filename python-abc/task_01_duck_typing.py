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

    @abstractmethod
    def area(self):
        """returning circle area"""
        return math.pi * (self.radius ** 2)

    @abstractmethod
    def perimeter(self):
        """"returning perimeter of circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class"""

    def __init__(self, width, height):
        """initialising rectangle"""
        self.width = width
        self.height = height

    @abstractmethod
    def area(self):
        """returning rectangle area"""
        return width * height

    @abstractmethod
    def perimeter(self):
        """returning perimeter of rectangle"""
        return (2 * width) + (2 * height)
