from numpy import *
r,c=[int(i) for i in input('Enter how many rows, cols: ').split()]
arr1=zeros((r,c),dtype=int)
arr2=zeros((r,c),dtype=int)
print('Enter elements for matrix 1 row by row')
for i in range(r):
    arr1[i]=[int(i) for i in input().split()]
print('Enter elements for matrix 2 row by row')
for i in range(r):
    arr2[i]=[int(i) for i in input().split()]
m1=matrix(arr1)
m2=matrix(arr2)
m3=m1+m2
print(m3)