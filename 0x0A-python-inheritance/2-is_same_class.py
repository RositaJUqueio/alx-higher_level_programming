#!/usr/bin/python3
# Rosita J Uqueio

"""Defining a class-checking function."""


def is_same_class(obj, a_class):
    """returns True if object is an instance of specified clas"""
    if type(obj) == a_class:
        return True
    return False
