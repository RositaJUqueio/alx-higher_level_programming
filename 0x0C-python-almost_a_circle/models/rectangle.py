#!/usr/bin/python3
# Rosita J Uqueio

"""Defines a Rectangle class """


class Rectangle(Base):
    """Rectangle inherits Base class"""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing and assigning values to attributes"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
