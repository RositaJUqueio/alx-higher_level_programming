#!/usr/bin/python3
# Rosita J Uqueio

def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char.lower() != 'c':
            new_string += char
    return (new_string)
