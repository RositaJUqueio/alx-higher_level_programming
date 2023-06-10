#!/usr/bin/python3
# Rosita J Uqueio

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for j in range(len(row)):
            print("{:d}{}".format(row[j], " " if j
                  != len(row) - 1 else ""), end="")
        print()
