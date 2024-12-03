def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    
a,b,c=[int(i) for i in input("Enter three no: ").split()]
res=greatest(a,b,c)
print("The greatest is %d" %res)
