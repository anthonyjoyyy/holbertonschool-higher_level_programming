#!/usr/bin/python3

# addition of all the arguments

if __name__ == "__main__":
    import sys    # for sys.argv

    total = 0

    for i in range(1, len(sys.argv)):
        total += int(sys.argv[i])    # int()

    print("{}".format(total))
