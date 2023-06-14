#!/usr/bin/python3
# Rosita J Uqueio

def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    ret = list(a_dictionary.keys())[0]
    large = a_dictionary[ret]
    for k, v in a_dictionary.items():
        if v > large:
            large = v
            ret = k
    return (ret)
