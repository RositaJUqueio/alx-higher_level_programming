#!/usr/bin/python3
# Rosita J Uqueio

"""
Function returns the sum of 'a' and 'b'
Float values are typecasted into integers.
Raises: TypeError if 'a' or 'b' are not integers.
"""

def add_integer(a, b=98):
    """Takes arguments 'a' & 'b'
    Returns:the sum of arguments
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
