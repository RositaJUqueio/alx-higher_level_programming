#!/usr/bin/python3
# Rosita J Uqueio

"""retrieve the value of the size attribute"""
 
class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = 0  # Initialize size to 0
        self.size = size  # setter method to set the size

    @property
    def size(self):
        """method to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size
