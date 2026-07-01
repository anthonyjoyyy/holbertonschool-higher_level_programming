#!/usr/bin/python3

# prints x integers of a list - only integers

def safe_print_list_integers(my_list=[], x=0):
    print_return = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list=[i], end=""))
            print_return += 1

        except (ValueError, TypeError):
            pass

    print("")

    return print_return
