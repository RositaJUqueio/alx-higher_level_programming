#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1

    '''program that prints the number of and the list of its arguments.
    Args: 
        n: Number of argument(s)
        string: Argument list
        pos: argument position
        '''
    if n == 1:
        print("{} argument:".format(n))
    elif n == 0:
        print("{} arguments.".format(n))
    else:
        print("{} arguments:".format(n))
    for arg in range(n):
            pos = arg + 1
            string = sys.argv[arg + 1]
            print("{}: {}".format(pos,string))
            
