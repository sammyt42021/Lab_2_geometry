# circle.py
import math


class Circle:
    def __init__(self, x=0, y=0, radius=1):

        # check that all values are numbers
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("x and y must be numbers")


        self._x = x
        self._y = y
        self.radius = radius

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    

    @property 
    def radius(self):
        return self._radius
    
    
    @radius.setter
    def radius(self, value):

        if not isinstance(value, (int, float)):
            raise TypeError("radius must be a number")

        if value <= 0:
            raise ValueError("radius must be greater than 0")
        
        self._radius=value
        
    @property
    def area(self):
        """Read-only area of the circle."""
        return math.pi * self.radius * self.radius

    @property
    def perimeter(self):
        """Read-only circumference of the circle."""
        return 2 * math.pi * self.radius



    def translate(self, dx, dy):
        """Move the circle by dx and dy."""
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise TypeError("dx and dy must be numbers")
        self._x += dx
        self._y += dy


#comparison operators
    def __eq__(self, other):
        """Circles are equal if they have the same radius."""
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius
    
    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius

    def __le__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius <= other.radius

    def __ge__  (self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius >= other.radius

    #extra checks

    def is_unit_circle(self):
        """Return True if the circle is centered at (0,0) and radius is 1."""
        return self.x == 0 and self.y == 0 and self.radius == 1


    def __repr__(self):
        """Unambiguous string, useful for debugging."""
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"

    def __str__(self):
        """User-friendly description."""
        return f"Circle with center ({self.x}, {self.y}) and radius{self.radius}"
