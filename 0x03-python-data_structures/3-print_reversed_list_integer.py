#!/usr/bin/python3
# Rosita J Uqueio

def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list, in reverse order"""
    for i in my_list:
        my_list.reverse()
        print("{:d}".format(my_list[i - 1]))
