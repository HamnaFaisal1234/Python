class Polygon:
    def calculate_area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius


rectangle = Rectangle(10, 5)
square = Square(4)
triangle = Triangle(6, 3)
circle = Circle(7)

print("Rectangle Area:", rectangle.calculate_area())
print("Square Area:", square.calculate_area())
print("Triangle Area:", triangle.calculate_area())
print("Circle Area:", circle.calculate_area())
