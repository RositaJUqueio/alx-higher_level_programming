#!/usr/bin/python3
# Rosita J Uqueio

def safe_print_division(a, b):
    """divides 2 integers and prints the result."""
    try:
        c = a / b
    except ZeroDivisionError:
        c = None
    finally:
        print("Inside result: {}".format(c))
    return c
