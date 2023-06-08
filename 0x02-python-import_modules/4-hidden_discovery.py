#!/usr/bin/python3
# Rosita J Uqueio

if __name__ == "__main__":
    """program prints names defined in module"""
    import hidden_4

    names = dir(hidden_4)
    for n in names:
        if n[:2] != '__':
            print(n)
