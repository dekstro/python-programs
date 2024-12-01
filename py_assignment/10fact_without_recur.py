# function to calculate factorial of a no
def fact(n):
    res=1   # i have taken an initial value 1 stored in res
    for i in range(1,n+1):  # loop to continue from 1 to n+1 number
        res=res*i       #result is stored in res var 1*1*2*3*4...
    return res
n=int(input("Enter a no: "))
res=fact(n)
print("Factorial of %d is %d" %(n,res))