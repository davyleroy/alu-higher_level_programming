#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle.
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.set_width(width)
        self.set_height(height)
        type(self).number_of_instances += 1

    def set_width(self, width):
        """Set the width of the Rectangle."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self._width = width

    def set_height(self, height):
        """Set the height of the Rectangle."""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self._height = height

    def get_width(self):
        """Get the width of the Rectangle."""
        return self._width

    def get_height(self):
        """Get the height of the Rectangle."""
        return self._height

    def area(self):
        """Return the area of the Rectangle."""
        return (self._width * self._height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self._width == 0 or self._height == 0:
            return 0
        return (self._width * 2 + self._height * 2)

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self._width == 0 or self._height == 0:
            return ""
        return "\n".join(["#" * self._width] * self._height)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
