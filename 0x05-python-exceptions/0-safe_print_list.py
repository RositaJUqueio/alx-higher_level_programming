#!/usr/bin/python3
# Rosita J Uqueio

def safe_print_list(my_list=[], x=0):
    "function that prints x elements of a list."
    count = 0
    try:
        for i in my_list[:x]:  # Iterate only up to x elements
            print(i, end="")
            count += 1
        print()
    except IndexError:
        print()  # Print a new line if the list is empty or shorter than x
    return count
