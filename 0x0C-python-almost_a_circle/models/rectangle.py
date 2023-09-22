#!/usr/bin/python3
# Rosita J Uqueio

"""Defines a Rectangle that inherits base class """
from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing and assigning value attributes.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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

    @property
    def x(self):
        """Retrieves x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x value"""
        self.__x = value

    @property
    def y(self):
        """Retrieves y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y value"""
        self.__y = value
