#!/usr/bin/python3
"""
Adds all arguments to a Python list, and then saves them to a file in JSON format.
"""

import sys
from os import path
from typing import List
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_item(args: List[str]) -> List[str]:
    """Adds all arguments to a Python list"""
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    items += args[1:]
    save_to_json_file(items, "add_item.json")
    return items

if __name__ == '__main__':
    items = add_item(sys.argv)
    print(items)

