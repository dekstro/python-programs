# Python program to find smallest number in a list
lst=[12,3,8,74,5,12,4]
res=min(lst)
print(res)

#another method
small=lst[0]
for i in lst:
    if i<small:
        small=i
print(small)
