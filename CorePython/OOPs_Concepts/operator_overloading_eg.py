class Shape:
    def draw(self):
        print("Drawing a shape")
        
class Circle(Shape):
    def draw(self):
        print("Drawing a circle")
        
class Square(Shape):
    def draw(self):
        print("Drawing a square")
        
#operator overloading example

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    
v1=Vector(2,3)
v2=Vector(4,5)
v3=v1+v2

print(v3.x,v3.y)
    