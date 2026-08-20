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

class Dragon(SwimMixing, FlyMixin):
    "class inheriting from both mixin classes"
