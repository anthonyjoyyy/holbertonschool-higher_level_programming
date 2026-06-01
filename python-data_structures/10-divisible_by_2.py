#!/usr/bin/python3

# function that finds whether the value is divisble by 2 or not

def divisible_by_2(my_list=[]):

    newlist = []

    for number in my_list:
        if number % 2 == 0:
            newlist.append(True)
        else:
            newlist.append(False)

    return newlist
