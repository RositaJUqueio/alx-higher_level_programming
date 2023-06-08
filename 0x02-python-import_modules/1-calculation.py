#!/usr/bin/python3
# Rosita J Uqueio

if __name__ == "__main__":
    """program does some maths"""
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
