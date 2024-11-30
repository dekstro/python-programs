def arithemetic_ops(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
a=int(input("Enter a no: "))
b=int(input("Enter a no: "))
r1,r2,r3,r4=arithemetic_ops(a,b)
print("Addition: ",r1)
print("Substraction: ",r2)
print("Multiplication: ",r3)
print("Division: ",r4)