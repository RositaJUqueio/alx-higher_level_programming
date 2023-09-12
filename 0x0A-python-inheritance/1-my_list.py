#!/usr/bin/python3
# Rosita J Uqueio

"""Defining an inherited list class MyList"""


class MyList(list):
    """Implements a sorted list"""
    
    def print_sorted(self):
        """Prints sorted list"""
        print(sorted(self))
