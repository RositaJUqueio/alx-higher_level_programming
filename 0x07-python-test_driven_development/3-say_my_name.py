#!/usr/bin/python3
# Rosita J Uqueio
"""Function prints First Name and Last Name"""


def say_my_name(first_name, last_name=""):
    """
    function prints:'My name is first_name last_name'
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
