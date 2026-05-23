#!/usr/bin/python3

# using dir() function to list variables alphabetically

if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)

    for x in names:
        if names[:2] != "__":
            print("{}".format(x))
