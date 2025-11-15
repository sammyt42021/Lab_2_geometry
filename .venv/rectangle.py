
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