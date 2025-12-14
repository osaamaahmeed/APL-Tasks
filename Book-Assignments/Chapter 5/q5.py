import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


shape1 = Shape()
shape2 = Rectangle(5, 10)
shape3 = Circle(5)

# print(shape1.area())
print(shape2.area())
print(shape3.area())
