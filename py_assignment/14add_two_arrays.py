from numpy import *
r,c=[int(i) for i in input('Enter how many rows and cols: ').split()]
arr1=zeros((r,c),dtype=int)
arr2=zeros((r,c),dtype=int)
arr3=zeros((r,c),dtype=int)
print('Enter elements in array 1')
for i in range(r):
    arr1[i]=[int(i) for i in input().split()]
print('Enter elements of array 2')
for i in range(r):
    arr2[i]=[int(i) for i in input().split()]
for i in range(r):
    arr3[i]=arr1[i]+arr2[i]
print("Sum is\n",arr3)
    