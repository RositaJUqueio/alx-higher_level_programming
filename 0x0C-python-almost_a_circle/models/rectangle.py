#!/usr/bin/python3
# Rosita J Uqueio

"""Defines a Rectangle that inherits base class """
from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing and assigning value attributes.

        Args:
          width (int): The width of new Rectangle.
          height (int): The height of new Rectangle.
          x (int): The x coordinate of new Rectangle.
          y (int): The y coordinate of new Rectangle.
          id (int): The identity of new Rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """Retrieves width value"""
            return self.__width

        @width.setter
        def width(self, value):
            """Sets width value"""
            self.__width = value

        @property
        def height(self):
            """Retrieves height value"""
            return self.__height

        @height.setter
        def height(self, value):
            """Sets height value"""
            self.__height = value
