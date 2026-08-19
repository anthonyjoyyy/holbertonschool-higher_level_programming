#!/usr/bin/python3
"""
the module contains an abstract class where inherited
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""
    @abstractmethod
    def sound(self):
        """Abstract method that returns the sound of the animal."""
        pass


class Dog(Animal):
    """class representing a dog"""
    def sound(self):
        """returns the sound of a dog"""
        return "Bark"


class Cat(Animal):
    """class representing a cat"""
    def sound(self):
        """returns the sound of a cat"""
        return "Meow"
