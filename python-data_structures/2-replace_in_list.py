#!/usr/bin/python3

# replacing a specific element in a list when given the index

def replace_in_list(my_list, idx, element):

    if idx < 0:  # if the index is a negative number, return the original list
        return my_list

    elif idx >= len(my_list):  # if the index is greater than the string
        return my_list

    else:
        my_list[idx] = element  # replace the index with the new element
        return my_list
