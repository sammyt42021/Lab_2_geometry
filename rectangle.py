
class Rectangle:
    def __init__(self, x: float, y: float, width: float, height: float):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("x and y must be numbers")

        self.x = x
        self.y = y
        self.width = width
        self.height = height


    @property
    def width(self) -> float:
        return self._width

    @width.setter 
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("width must be a number")
        if value <= 0:
            raise ValueError("width must be greater than 0")
        self._width = value


    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("height must be a number")
        if value <= 0:
            raise ValueError("height must be greater than 0")
        self._height = value

    @property
    def area(self) -> float:
        """Read-only area."""
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        """Read-only perimeter."""
        return 2 * (self.width + self.height)

    def translate(self, dx, dy)-> None:
        """Move the rectangle."""
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise TypeError("dx and dy must be numbers")
        self.x += dx
        self.y += dy


  # Comparison operators
    def __eq__(self, other)-> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.width == other.width and self.height == other.height

    def __gt__(self, other)-> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area > other.area

    def __lt__(self, other)-> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area < other.area

    def __le__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area <= other.area

    def __ge__(self, other)-> bool: 
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area >= other.area   
    

    def is_square(self)-> bool:
        """Return True if width == height."""
        return self.width == self.height
    


    def __repr__(self)-> str:
        """Unambiguous developer representation."""
        return f"Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height})"

    def __str__(self)-> str:
        """User-friendly description."""
        return f"Rectangle with center ({self.x}, {self.y}), width {self.width}, height {self.height}"
