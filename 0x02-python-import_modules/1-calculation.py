#!/usr/bin/python3
# if __name__ == '__main__' checks if a file is imported as a module.
if __name__ == "__main__":
    # code won't run if file is imported

    from calculator_1 import add, sub, mul, div

    ''' program imports functions from file,
    does some math and prints result
    '''
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
