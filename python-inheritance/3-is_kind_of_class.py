#!/usr/bin/python3
"""
This modules defines a function and checks inherited instances
"""


def is_kind_of_class(obj, a_class):
    """ Checks if the object is instance of class or inherited from"""
    return isinstance(obj, a_class)
