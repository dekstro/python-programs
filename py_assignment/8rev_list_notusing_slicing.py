lst=[10,20,5,4,33,22]
i=0
j=len(lst)-1
while i<=j:
    temp=lst[i]
    lst[i]=lst[j]
    lst[j]=temp
    i+=1
    j-=1
print(lst)

