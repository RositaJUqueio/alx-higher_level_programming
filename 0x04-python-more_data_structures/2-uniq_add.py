#!/usr/bin/python3
# Rosita J Uqueio

def uniq_add(my_list=[]):
    """Adds all unique integers in a list (once for each integer)."""
    result = 0
    for x in set(my_list):
        result += x
    return (result)
