#!/usr/bin/python3
"""
module contains "mastering mixins".
"""


class SwimMixin:
    "swimmixin class"

    def swim(self):
        "method that prints message"
        print("The creature swims!")


class FlyMixin:
    "flymixin class"

    def fly(self):
        "method that prints message"
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    "class inheriting from both mixin classes"

    def roar(self):
        "if the dragon roars"
        print("The dragon roars!")
