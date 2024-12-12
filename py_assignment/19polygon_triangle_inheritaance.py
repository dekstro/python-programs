class Polygon:
    def inputSides(self,x):
        self.x=x
        self.a,self.b,self.c=[float(i) for i in input('Enter sides: ').split()]
class Triangle(Polygon):
    def __init__(self):
        super().__init__()
    def area(self):
        s=(self.a + self.b + self.c)/2
        area=(s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
        return area
t=Triangle()
t.inputSides(3)
res=t.area()
print('The area of triangle is',res)