#!/usr/bin/python3
# Rosita J Uqueio

def complex_delete(a_dictionary, value):
    """ function deletes keys with a specific value in a dictionary."""
    while value in a_dictionary.values():
        for k, v in a_dictionary.items():
            if v == value:
                del a_dictionary[k]
                break

    return (a_dictionary)
