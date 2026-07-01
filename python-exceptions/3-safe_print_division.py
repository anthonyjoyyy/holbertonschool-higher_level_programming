#!/usr/bin/python3

# divide 2 integers and print the result

def safe_print_division(a, b):
    result = None

    try:
        result = a/b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))

    return result
