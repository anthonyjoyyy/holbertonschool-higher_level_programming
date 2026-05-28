#!/usr/bin/python3

# replacing a specific element in a list when given the index

def replace_in_list(my_list, idx, element):

    my_list[idx] = "element"

        if idx < 0:
            return my_list

        elif idx >= len(my_list):
            return my_list

        else:
            return my_list[idx]
