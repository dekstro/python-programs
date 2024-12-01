def fact(n):
    res=1
    for i in range(1,n+1):
        res=res*i
    return res
n=int(input("Enter a no: "))
res=fact(n)
print("Factorial of %d is %d" %(n,res))