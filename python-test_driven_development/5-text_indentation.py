#!/usr/bin/python3
"""
This module contains a function that prints a text in a specific format.
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    skip = True

    for i in range(len(text)):
        if skip and char == " ":
            continue

        skip = False

        print(text[i], end="")

        if text[i] in [".", "?", ":"] and i != len(text) - 1:
            print()
            print()
            skip = True
