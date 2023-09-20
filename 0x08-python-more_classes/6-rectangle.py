#!/usr/bin/python3
# Rosita J Uqueio
class Rectangle:
    """Defines a rectangle."""

    number_of_instances = 0
    # keeps track of the number of Rectangle instances created.

    def __init__(self, width=0, height=0):
        """Initialize a rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        # incrementing Rectangle instances withe each creation

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
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method to set the height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        """Returns a string representation of the rectangle to recreate it."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a farewell message when the instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        # decrementing instances with each deletion
