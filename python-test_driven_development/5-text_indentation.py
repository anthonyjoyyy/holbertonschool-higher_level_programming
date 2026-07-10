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

    for char in text:
        if skip and char == " ":
            continue

        skip = False

        print(char, end="")

        if char in [".", "?", ":"]:
            print("\n")
            skip = True
