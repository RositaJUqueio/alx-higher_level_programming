#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order."""
    if isinstance(my_list, list):
        # isinstance() that compares the value with the type given.
        my_list.reverse()
        for i in my_list:
            print("{}".format(i))
