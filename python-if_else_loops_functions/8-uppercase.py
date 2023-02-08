#!/usr/bin/python3
def uppercase(str):
    new = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            char = ord(char) - 32
            new += chr(char)
        else:
            new += char
    print("{}".format(new))
