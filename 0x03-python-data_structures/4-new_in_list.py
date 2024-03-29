#!/usr/bin/python3
# Rosita J Uqueio

def new_in_list(my_list, idx, element):
    """function replaces an element in a list at a specific position"""
    my_list = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list

    my_list[idx] = element
    return my_list
