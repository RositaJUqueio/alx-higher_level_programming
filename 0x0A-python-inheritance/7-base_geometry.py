#!/usr/bin/python3
# Rosita J Uqueio

"""Defining a base geometry class BaseGeometry"""


class BaseGeometry:
    """Representing BaseGeometry"""
    pass

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function validates value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
