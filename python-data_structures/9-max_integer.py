#!/usr/bin/python3

# find biggest integer in the list

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max = my_list[0]

    for x in my_list:
        if x > max:
            max = x

    return max
