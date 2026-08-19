#!/usr/bin/python3
"""
This module defines a VerboseList class
"""


class VerboseList(list):
    """custom list class with print messages"""

    def append(self, item):
        """Add item to list and print message"""
        super().append(item)
        print("Added {} to the list.".format(item))

    def extend(self, items):
        """Extending list and printing message"""
        super().extend(items)
        print("Extended the list with {} items.".format(len(items)))

    def remove(self, item):
        """removing item and printing message"""
        print("Removed {} from the list.".format(item))
        super().remove(item)

    def pop(self, item=-1):
        """picking a particular item and printing message"""
        popped_item = super().pop(item)
        print("Popped [{}] from the list.".format(popped_item))
        return popped_item
