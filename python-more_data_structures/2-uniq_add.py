#!/usr/bin/python3

# add integers once via set()

def uniq_add(my_list=[]):
    empty = set(my_list)
    total = 0

    for integer in empty:
        total += integer

    return total
