#!/usr/bin/python3
# Rosita J Uqueio

"""Defining a class-checking function."""


def is_kind_of_class(obj, a_class):
    """
    Return: True if the object is an instance of,
     /if the object is an instance of a class that inherited from,
     the specified class"""
    if isinstance(obj, a_class):
        return True
    return False
