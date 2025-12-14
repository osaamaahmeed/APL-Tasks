class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return (self.x * other.x) + (self.y * other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(5, 10)
v2 = Vector(2, 3)

v3 = v1 - v2
print(f"Subtraction: {v1} - {v2} = {v3}")

dot_prod = v1 * v2
print(f"Dot Product: {v1} * {v2} = {dot_prod}") 