#!/usr/bin/python3
# Rosita J Uqueio

def no_c(my_string):
    """function removes all characters c and C from a string"""
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
