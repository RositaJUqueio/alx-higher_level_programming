#!/usr/bin/python3
# Rosita J Uqueio

"""script that adds all arguments to a Python list"""
import sys
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    with open(filename) as file:
        return json.load(file)


if __name__ == "__main__":
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
