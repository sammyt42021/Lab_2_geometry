class Circle:
    def __init__(self, x, y, radius):
        # basic type checks
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("x and y must be numbers")

        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")

        if radius <= 0:
            raise ValueError("radius must be greater than 0")

        self.x = x
        self.y = y
        self.radius = radius
