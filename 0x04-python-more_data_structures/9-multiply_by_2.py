#!/usr/bin/python3
# Rosita J Uqueio

def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multipled by 2."""
    return ({k: a_dictionary[k] * 2 for k in a_dictionary})
