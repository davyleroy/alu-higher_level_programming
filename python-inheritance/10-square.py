#!/usr/bin/python3
""" Base Geometry Class """


class BaseGeometry:
    """ class that improves geometry with integer validator"""
    def area(self):
        """ raises an Exception with the message area() is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if (type(value) is not int):
            raise TypeError(name + " must be an integer")
        if (value <= 0):
            raise ValueError(name + " must be greater than 0")

""" Program that builds a full square """


class Square(BaseGeometry):
    """ class Square that inherits from BaseGeometry """
    def __init__(self, side):
        """ Constructor """
        self.__side = side
        BaseGeometry.integer_validator(self, "side", self.__side)

    def area(self):
        """ method that returns the area of square """
        return self.__side ** 2

    def __str__(self):
        """ string representation """
        return "[Square] " + str(self.__side) + " x " + str(self.__side)

