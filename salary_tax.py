def monthly_sal(a):
    salary=a/12
    return salary
def tax_func():
    a=int(input("Enter annual salary: "))
    salary=monthly_sal(a)
    print("Monthly salary is: ",salary)
    tax=salary*(10/100)
    return salary-tax
t=tax_func()
print("Salary after tax deduction is: ",t)
