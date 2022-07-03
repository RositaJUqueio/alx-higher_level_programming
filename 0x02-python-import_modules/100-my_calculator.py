#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    arguments = len(sys.argv) - 1
    mid = {"+": add, "-": sub, "*": mul, "/": div}
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    result = ("a sys.argv[2] b")
        
    if arguments != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] not in list(mid.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
    else:
        print("{} {} {} = {}".format(a, sys.argv[2],  b, result) 
