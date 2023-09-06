#!/usr/bin/python3
# Rosita J Uqueio
"""Module defines a matrix multiplication function using NumPy."""
import numpy as n


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices."""

    return (n.matmul(m_a, m_b))
