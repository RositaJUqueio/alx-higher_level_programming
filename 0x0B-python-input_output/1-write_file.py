#!/usr/bin/python3
# Rosita J Uqueio

""""Function writes a string to a text file"""
def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters written."""
    num_characters = 0
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        num_characters = len(text)
    return num_characters

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
