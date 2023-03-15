#!/usr/bin/python3
"""Write a class Square that defines a square by"""


class Square:
    """Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0)
    Public instance method: def area(self): that returns the square area
    Public instance mthd: def my_print(self): that prints the square with #
        no import modules"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for s in range(self.__size):
                    print('#', end="")
                print()
