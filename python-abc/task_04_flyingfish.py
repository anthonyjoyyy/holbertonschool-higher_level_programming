#!/usr/bin/python3
"""
a module exploring multiple intheritance. inheriting from multiple classes.
"""


class Fish:
    """fish class"""
    def swim(self):
        """if the fish is swimming"""
        print("The fish is swimming")

    def habitat(self):
        """the fish's habitat"""
        print("The fish lives in water")


class Bird:
    "bird class"
    def fly(self):
        "bird is flying"
        print("The bird is flying")

    def habitat(self):
        "where the bird lives"
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    "inheriting from two classes"
    def swim(self):
        "overriding swim method"
        print("The flying fish is swimming!")

    def fly(self):
        "overriding fly method"
        print("The flying fish is soaring!")

    def habitat(self):
        "overriding habitat method"
        print("The flying fish lives both in water and the sky!")
