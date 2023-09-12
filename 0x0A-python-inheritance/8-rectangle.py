#!/usr/bin/python3
# Rosita J Uqueio

"""Defining a class tha inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents rectangle"""

    def __init__(self, width, height):
        """initializing rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
