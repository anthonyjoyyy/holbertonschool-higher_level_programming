#!/usr/bin/python3

# using command-line and argv

if__name__ == "__main__":
    import sys

    x = len(sys.argv) - 1

    if x == 0:
        print("0 arguments.")

    elif x = 1:
        print("1 argument.")
    print("1: {}".format(sys.argv[1]))

    else:
        print("{} arguments".format(x))

    for p in range(1, x + 1):
        print("{}:{}".format(p, sys.argv[p]))
