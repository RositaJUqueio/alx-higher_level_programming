#!/usr/bin/python3
''' program that prints the result of the addition of all arguments
'''
if __name__ == "__main__":
    import sys
    result = 0
    # len(sys.argv) , checks how many arguments that have been entered.
    for a in range(len(sys.argv) - 1):
        result += int(sys.argv[a + 1])
        print("{}".format(result))
