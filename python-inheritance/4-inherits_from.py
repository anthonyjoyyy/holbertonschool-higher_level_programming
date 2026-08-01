#!/usr/bin/python3
"""
This module defines a function that checks inherited instances.
"""


def inherits_from(obj, a_class):
    """
    if object is directly or indirectly inherited
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
