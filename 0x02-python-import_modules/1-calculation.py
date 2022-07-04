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
    ans1 = add(a, b)
    ans2 = sub(a, b)
    ans3 = mul(a, b)
    ans4 = div(a, b)

    print(f"{a} + {b} = {ans1}")
    print(f"{a} - {b} = {ans2}")
    print(f"{a} * {b} = {ans3}")
    print(f"{a} / {b} = {ans4}")
