#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1

    '''program that prints the number of and the list of its arguments.
    Args: 
        n: Number of argument(s)
        string: Argument list
        '''
    for args in range(n):
        pos = args + 1
        string = sys.argv[args + 1]
        if n == 1:
            print("{} argument:".format(n))
            print("{}: {}".format(pos, string))
        elif n == 0:
            print("{} arguments.".format(n))
        else:
            print("{} arguments:".format(n))
            print("{:} {}".format(pos, string))
