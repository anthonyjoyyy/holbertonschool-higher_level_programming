#!/usr/bin/python3

# copy a list and edit the copied list, then return it

# function prototype
def new_in_list(my_list, idx, element):

    # checking the safeguards first
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()

    # now edit the element in the copied list
    else:
        the_list = my_list.copy()
        the_list[idx] = element
        return the_list
