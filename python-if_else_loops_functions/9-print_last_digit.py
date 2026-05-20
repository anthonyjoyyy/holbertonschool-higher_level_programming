#!/usr/bin/python3

# print the last digit of an integer, regardless if it's positive or negative

def print_last_digit(number):
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit
