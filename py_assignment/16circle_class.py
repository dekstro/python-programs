class Circle:
    def __init__(self,r=5):
        self.r=r
    def area(self):
        print('Area is',3.15*self.r*self.r)
c=Circle()
c.area()
c1=Circle(3)
c1.area()