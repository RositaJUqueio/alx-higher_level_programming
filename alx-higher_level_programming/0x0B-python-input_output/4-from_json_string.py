#!/usr/bin/python3
# Rosita J Uqueio

"""Defines a text file-appending function."""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a UTF8 text file.
    Returns:The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
