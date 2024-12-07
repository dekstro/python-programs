class Student:
    def __init__(self):
        self.rno = 15
        self.name = 'Raghav'
        self.addr='Puri, Odisha'
        self.marks = [93,99,90]
    def display(self):
        print('Roll no:',self.rno)
        print('Name:',self.name)
        print('Address:',self.addr)
        total=sum(self.marks)
        print('Total marks:',total)
        percentage=total/len(self.marks)
        print('Percentage of marks:',percentage)
s1=Student()
s1.display()



