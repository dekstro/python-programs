# Python program to print even numbers in a list
lst=[12,5,3,6,7,4]
obj=filter(lambda x: x%2==0,lst)
print(list(obj))

#another method
res=[]
for i in lst:
    if i%2==0:
        res.append(i)
print(res)