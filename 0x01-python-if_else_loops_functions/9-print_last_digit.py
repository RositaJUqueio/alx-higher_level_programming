#!/usr/bin/python3
# Rosita J Uqueio
def print_last_digit(number):
    """Function prints last digit"""
    last_digit = abs(number) % 10
    print("{:d}".format(last_digit), end="")
    return (last_digit)
