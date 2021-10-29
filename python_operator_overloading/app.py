import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def setRadius(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def area(self):
        return math.pi * self.__radius ** 2
    
    def __add__(self, circle_object):
        return Circle(self.__radius + circle_object.__radius)

    def __lt__(self, circle_object):
        return (self.__radius < circle_object.__radius)

    def __gt__(self, circle_object):
        return (self.__radius > circle_object.__radius)

    def __str__(self):
        return f"Circle area = {self.area()}"

    def __repr__(self):
        return f"Circle(radius={self.__radius})"

c1 = Circle(2)
c2 = Circle(3)
c3 = c1 + c2

print(c1.getRadius())
print(c2.getRadius())
print(c3.getRadius())
print(c3.getRadius())

print(c1<c2)
print(c1>c2)

print(c1)
print(repr(c1))
