#!/usr/bin/python3

# FizzBuzz

def fizzbuzz():
    for fb in range(0,101):
        if fb % 15 == 0:
        print("FizzBuzz")
        elif fb % 5 == 0:
        print("Buzz")
        elif fb % 3 == 0:
         print("Buzz")
        else:
        print(fb)
