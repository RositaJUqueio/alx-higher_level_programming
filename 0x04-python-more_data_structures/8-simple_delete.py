#!/usr/bin/python3
# Rosita J Uqueio

def simple_delete(a_dictionary, key=""):
    """function deletes a key in a dictionary."""
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
