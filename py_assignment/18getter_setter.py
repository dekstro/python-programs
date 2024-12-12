class Manager: #id, name, deptname, salary, gender (M or F)
    def getId(self,id):
        self.id=id
    def setId(self):
        return self.id
    def getName(self,name):
        self.name=name
    def setName(self):
        return self.name
    def getDeptname(self,deptname):
        self.deptname=deptname
    def setDeptname(self):
        return self.deptname
    def getSalary(self,salary):
        self.salary=salary
    def setSalary(self):
        return self.salary
    def getGender(self,gender):
        self.gender=gender
    def setGender(self):
        return self.gender
m=Manager()
m.getId(1)
print('Id:',m.setId())
m.getName('Rakesh')
print('Name:',m.setName())
m.getDeptname('IT')
print('DeptName:',m.setDeptname())
m.getSalary(50000)
print('Salary:',m.setSalary())
m.getGender('M')
print('Gender:',m.setGender())
