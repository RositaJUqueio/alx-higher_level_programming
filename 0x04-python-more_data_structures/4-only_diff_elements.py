#!/usr/bin/python3
# Rosita J Uqueio

def only_diff_elements(set_1, set_2):
    """Returns set of all elements present in only one set."""
    return (set_1 ^ set_2)