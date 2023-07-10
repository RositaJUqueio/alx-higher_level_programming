#!/usr/bin/python
# Rosita J Uqueio

"""Defining a class BaseGeometry."""


class BaseGeometry:
    """Represent the base geometry class."""

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: Raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value as an integer.

        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: Raises a TypeError exception if the value is not an integer.
            ValueError: Raises a ValueError exception if the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
