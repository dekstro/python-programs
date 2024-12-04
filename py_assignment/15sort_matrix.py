from numpy import *
r,c=[int(i) for i in input('Enter how many rows and cols: ').split()] 
str=input('Enter elements:\n') 
a=matrix(str)
m=reshape(a, (r,c))
s1=sort(m)[:, ::-1]
s2=sort(s1,axis=0)[::-1]
print('Matrix is\n',m)
print('Sorted on rows\n',s1)
print('Sorted on cols\n',s2)