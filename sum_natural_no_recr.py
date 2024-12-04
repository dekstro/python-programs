def sum(n):
    if n==1: return 1
    return n+sum(n-1)
n=int(input('Enter a no: '))
res=sum(n)
print("Sum of nth natural no is",res)