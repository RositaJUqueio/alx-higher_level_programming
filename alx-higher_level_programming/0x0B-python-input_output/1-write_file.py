#!/usr/bin/python3
# Rosita J Uqueio

"""Defineing a text file line-counting function."""


def number_of_lines(filename=""):
    """Returns the number of lines in a text file."""
    line_num= 0
    with open(filename) as f:
        for line_num in f:
            line_num += 1
    return line_num
