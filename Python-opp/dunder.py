# ----------------------- magic method and dunder (__) -----------------------

class Person:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # deletes the person object from the database
    def __del__(self):
        print('object being deleted')


person1 = Person('samuel', 70)
print(person1.name)
print(person1.marks)
print()


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)


v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2
print(v3)
