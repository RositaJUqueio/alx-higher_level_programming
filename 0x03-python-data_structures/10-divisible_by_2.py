#!/usr/bin/python3
# Rosita J Uqueio

def divisible_by_2(my_list=[]):
    """function finds all multiples of 2 in a list."""
    multiples = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return (multiples)
