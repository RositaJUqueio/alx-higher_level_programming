#!/usr/bin/python3
# Rosita J Uqueio

"""class defines a rectangle, returns area and perimeter"""


class Rectangle:
    """Defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = 0
        self.width = width  # setter method to set the width
        self.__height = 0
        self.height = height  # setter method to set the height

    @property
    def width(self):
        """Getter method to retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method to set the width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method to retrieve the height."""
        return (self.__width * self.__height)

    @height.setter
    def height(self, value):
        """Setter method to set the height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width + self.__height * 2)
