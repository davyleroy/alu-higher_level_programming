#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    new = ""
    for char in str:
        if i != n:
            new += char
        i += 1
    return (new)
