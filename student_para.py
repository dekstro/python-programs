class Student:
    def __init__(self,rno,name,addr,marks):
        self.rno=rno
        self.name=name
        self.addr=addr
        self.marks=marks
    def display(self):
        print('Roll no:',self.rno)
        print('Name:',self.name)
        print('Address:',self.addr)
        total=sum(self.marks)
        print('Total marks:',total)
        percentage=total/len(self.marks)
        print('Percentage of marks:',percentage)
s1=Student(15,'Raghav','Puri, Odisha',[93,99,90])
s1.display()



