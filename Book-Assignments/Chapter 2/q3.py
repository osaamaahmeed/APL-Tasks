class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Points: ( X:{self.x}, Y:{self.y} )"

p1 = Point(5,7)
print(p1)

p1.x = 9
print(p1)

p1.z = 1
print(p1)

# AttributeError: 'Point' object has no attribute 'z'
'''
Defining __slots__ tells Python to freeze the object's structure and only reserve memory for the specific variables I list (like x and y)
Because the object is no longer flexible, there is physically no space allocated to store a new variable like z, so the program crashes when you try to add it.
This feature is mainly used to save memory when you are creating millions of small objects.
'''