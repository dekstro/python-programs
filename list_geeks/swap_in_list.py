#Python Program to Swap Two Elements in a List
lst=[1,10,2,5,9]
a,b=[int(i) for i in input('Enter positions to swap(0-5): ').split()]
print(lst)
temp=lst[a]
lst[a]=lst[b]
lst[b]=temp
print(lst)

