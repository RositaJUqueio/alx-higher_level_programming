#!/usr/bin/python3
# Rosita J Uqueio

if __name__ == "__main__":
    """Prints the number of & list of arguments."""
    import sys

    argv = len(sys.argv) - 1
    if argv == 0:
        print("0 arguments.")
    elif argv == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argv))
    for i in range(argv):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
