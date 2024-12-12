class Father:
    def __init__(self):
        self.father_property=500000
class Mother:
    def __init__(self):
        self.mother_property=400000
class Child(Father,Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
    def display(self):
        self.child_property=self.father_property+self.mother_property
        print('Child Property is',self.child_property)
c=Child()
c.display()