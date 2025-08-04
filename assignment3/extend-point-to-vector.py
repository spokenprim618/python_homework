import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def equality(self,point2):
        return "They are equal" if self.x == point2.x and self.y == point2.y else "They are not"
    def string(self):
        return f"({self.x},{self.y})"
    def distance(self,point2):
        return math.sqrt(((point2.x-self.x)**2)+((point2.y-self.y)**2))
    
class Vector(Point):
    def __init__(self,x,y):
        super().__init__(x,y)
    def string(self):
        return f"<{self.x},{self.y}>"
    def __add__(self, vector2):
        return Vector(self.x + vector2.x, self.y + vector2.y)

point1 = Point(5,6)
point2 = Point(10,9)
vector1 = Vector(1,2)
vector2 = Vector(2,3)
print(point1.equality(point2))
print(point2.distance(point1))
print(point1.string())
print(vector1.string())
print(vector1+vector2)
