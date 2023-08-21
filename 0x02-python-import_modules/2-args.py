#!/usr/bin/python3
# Rosita J Uqueio

if __name__ == "__main__":
    """Prints the number of & list of arguments."""
    import sys

    num_args = len(sys.argv) - 1
    args = sys.argv

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))
    for index in range(num_args):
        print("{}: {}".format(index + 1, args[index + 1]))
