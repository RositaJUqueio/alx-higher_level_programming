#!/usr/bin/python3
# Rosita J Uqueio

"""Function reads a text file (UTF8) &  prints it to stdout"""


def read_file(filename=""):
    """Print contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
