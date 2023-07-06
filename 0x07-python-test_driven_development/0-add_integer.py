#!/usr/bin/python3
# Rosita J Uqueio

def add_integer(a, b=98):
    """Function that adds 2 integers"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    a = int(a)
    b = int(b)
    return a + b
