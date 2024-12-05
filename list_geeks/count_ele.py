#Count occurrences of an element in a list in Python
lst=[12,10,25,1,6,5,10]
n=int(input('Enter no to find: '))
count=0
for i in lst:
    if i==n:
        count+=1
print(count)