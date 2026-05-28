#!/usr/bin/python3

# remove all C's, regardless whether it's lowercase or uppercase

def no_c(my_string):
    new_string = ""  # empty basket, creating the new string

    for c in new_string:
        if c != 'c' and c != 'C':
            new_string += c

            return new_string
