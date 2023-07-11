#!/usr/bin/python3
# Rosita J Uqueion

""""Function writes a string to a text file"""


def number_of_lines(filename=""):
    """Returns number of lines in a text file."""
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
    return lines
