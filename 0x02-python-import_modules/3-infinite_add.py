#!/usr/bin/python3
# Rosita J Uqueio

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    num_args = len(sys.argv) - 1
    args = sys.argv

    total = 0
    for i in range(num_args):
        total = total + int(args[i + 1])
    print("{}".format(total))
