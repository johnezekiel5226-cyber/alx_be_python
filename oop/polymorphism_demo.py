import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the area() method.")


# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Demonstration of polymorphism
if __name__ == "__main__":
    shapes = [
        Rectangle(5, 3),  # Area: 15
        Circle(4),        # Area: ~50.27
        Rectangle(2, 7),  # Area: 14
        Circle(1)         # Area: ~3.14
    ]

    for shape in shapes:
        print(f"{shape.__class__.__name__} area: {shape.area():.2f}")
