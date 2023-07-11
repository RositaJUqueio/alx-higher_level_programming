#!/usr/bin/python3
# Rosita J Uqueio

"""function returns the dictionary description with simple data struct"""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
