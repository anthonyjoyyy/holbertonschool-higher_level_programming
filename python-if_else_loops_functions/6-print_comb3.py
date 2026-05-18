#!/usr/bin/python3

# printing all 2 digit numbers up to 100 without repeating the same two digits

for i in range(9):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
