class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2* (self.width + self.height)

rec1 = Rectangle(5,10)

print(f"The Rectangle is {rec1.width} x {rec1.height}")
print(f"Area: {rec1.area()}")
print(f"Permimeter: {rec1.perimeter()}")