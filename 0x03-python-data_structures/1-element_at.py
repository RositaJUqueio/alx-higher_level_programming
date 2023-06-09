#!/usr/bin/python3
# Rosita J Uqueio

def element_at(my_list, idx):
    """function retrieves an element from a list """
    if idx < 0 or idx > len(my_list) - 1:
        return None
    return (my_list[idx])
