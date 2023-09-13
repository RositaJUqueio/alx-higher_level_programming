#!/usr/bin/python3
# Rosita J Uqueio

"""Defines a text file-writing function."""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF8 text file.
    Returns: Number of written characters.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
