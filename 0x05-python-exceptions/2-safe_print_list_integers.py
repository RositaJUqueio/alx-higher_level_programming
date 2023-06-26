#!usr/bin/python3
# Rosita J Uqueio

def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list & only integers."""
    count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(int(i)), end="")
                count = count + 1
        print()
    except (IndexError, TypeError):
        pass
    return count
