#!/usr/bin/python3
# Rosita J Uqueio

"""Defining a Pascal's Triangle function."""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    shape = [[1]]
    while len(shape) != n:
        tri = shape[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        shape.append(tmp)
    return shape
