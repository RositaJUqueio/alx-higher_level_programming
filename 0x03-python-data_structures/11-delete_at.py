#!/usr/bin/python3
# Rosita J Uqueio

def delete_at(my_list=[], idx=0):
    """function deletes the item at a specific position"""
    if idx < 0 or idx > len(my_list) - 1:
        return my_list

    del my_list[idx]
    return my_list
