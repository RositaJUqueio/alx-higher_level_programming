#!/usr/bin/python3
# Rosita J Uqueio

"""Function writes a string to a text files"""


def write_file(filename="", text=""):
    """"Returns the number of characters written"""
    char_count = 0

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        char_count = len(text)

    return char_count
