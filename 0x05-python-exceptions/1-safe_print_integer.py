#!/usr/bin/python3
# Rosita J Uqueio

def safe_print_integer(value):
    """function that prints an integer"""
    try:
        print("{:d}".format((value)))
        return True
    except (ValueError, TypeError):
        # exception flags value conversion or format
        return False
