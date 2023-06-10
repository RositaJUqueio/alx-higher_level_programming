#!/usr/bin/python3
# Rosita J Uqueio

def new_in_list(my_list, idx, element):
    lists = list(my_list)
    if idx < 0 or idx >= len(my_list):
        return (lists)
    else:
        lists[idx] = element
        return (lists)
