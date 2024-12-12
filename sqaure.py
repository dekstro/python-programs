class Sqaure:
    def __init__(self,x):
        self.x=x
    def area(self):
        print('Area of sqaure=',self.x*self.x)
class Rectangle(Sqaure):
    def __init__(self, x,y):
        super().__init__(x)
        self.y=y
    def area(self):
        print('Area of rectangle=',self.x*self.y)
r=Rectangle(7,4)
r.area()
        