#!/usr/bin/python3
"""Write a class Square that defines a square by"""


class Square:
    """Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0)
    no module import"""
    def __init__(self, size=0):
        """ initialize the square 
            Args inputs
                size in (int): square size
            """
        if  type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

