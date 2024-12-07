class Person:
    def __init__(self):
        self.name='Krishna'
        self.age=22
    def talk(self):
        print('Hello',self.name)
        print('Age',self.age)
p1=Person()
p1.talk()