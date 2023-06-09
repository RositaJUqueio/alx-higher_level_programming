#!/usr/bin/python3
# Rosita J Uqueio

def replace_in_list(my_list, idx, element):
    """function replaces element of list at specific position"""
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list)
    my_list[idx] = element
    return (my_list)
