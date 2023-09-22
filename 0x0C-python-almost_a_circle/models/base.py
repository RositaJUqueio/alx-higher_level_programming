#!/usr/bin/python3
# Rosita J Uqueio

"""Defining class Base"""
import json
import csv
import turtle

class Base:
    """Writing first class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
