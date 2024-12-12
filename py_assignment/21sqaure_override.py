class Sqaure:
    def __init__(self,x):
        self.x=x
    def calc(self):
        self.res=self.x*self.x
        print(self.res)
class Cube(Sqaure):
    def __init__(self, x):
        super().__init__(x)
    def calc(self):
        self.res=self.x*self.x*self.x
        print(self.res)
c=Cube(2)
c.calc()
