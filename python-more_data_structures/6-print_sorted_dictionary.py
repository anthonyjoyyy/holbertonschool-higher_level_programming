#!/usr/bin/python3

# order the keys in a string

def print_sorted_dictionary(a_dictionary):

    # 1. Grab all the keys and organize them alphabetically
    alphakeys = sorted(a_dictionary.keys())

    # 2. Loop through our perfectly ordered list of keys
    for key in alphakeys:

        # 3. Pull out the value attached to this specific key
        value = a_dictionary[key]

        # 4. Print them out in the requested "Key: Value" format
        print("{}: {}".format(key, value))
