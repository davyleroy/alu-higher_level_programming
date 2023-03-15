class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    def set_width(self, width):
        """Set the width of the Rectangle."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.width = width

    def set_height(self, height):
        """Set the height of the Rectangle."""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.height = height

    def get_area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def get_perimeter(self):
        """Return the perimeter of the Rectangle."""
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.width == 0 or self.height == 0:
            return ""

        rect = ""
        for i in range(self.height):
            rect += "#" * self.width + "\n"

        return rect[:-1]

    def get_picture(self):
        """Return a string representation of the Rectangle with # characters."""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        return str(self)

    def get_amount_inside(self, shape):
        """Return the number of times the given shape can fit inside the Rectangle."""
        return self.get_area() // shape.get_area()

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")

