#!/usr/bin/python3
# Rosita J Uqueio

"""function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line
    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as n:
        for line in n:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
