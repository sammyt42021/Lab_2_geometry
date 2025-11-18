
class Rectangle:
    def __init__(self, x, y, width, height):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("x and y must be numbers")

        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("width and height must be numbers")

        if width <= 0 or height <= 0:
            raise ValueError("width and height must be greater than 0")

        self.x = x
        self.y = y
        self.width = width
        self.height = height


    @property
    def area(self):
        """Read-only area."""
        return self.width * self.height

    @property
    def perimeter(self):
        """Read-only perimeter."""
        return 2 * (self.width + self.height)

    def translate(self, dx, dy):
        """Move the rectangle."""
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise TypeError("dx and dy must be numbers")
        self.x += dx
        self.y += dy