#!/usr/bin/python3
# Rosita J uqueio
"""Module defines a square-printing function."""


def print_square(size):
    """Print a square using the # character.

    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for n in range(size):
        [print("#", end="") for n in range(size)]
        print("")
