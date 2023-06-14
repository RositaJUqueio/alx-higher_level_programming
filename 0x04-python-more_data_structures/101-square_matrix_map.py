#!/usr/bin/python3
# Rosita J Uqueio

def square_matrix_map(matrix=[]):
    return (list(map(lambda x: list(map(lambda y: y ** 2, x[:])), matrix)))
