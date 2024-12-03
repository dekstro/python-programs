from numpy import *
r,c=[int(i) for i in input('Enter how many rows, cols: ').split()]
arr=zeros((r,c),dtype=int)
print('Enter array elements row by row')
for i in range(r):
    arr[i]=[int(i) for i in input().split()]
m=matrix(arr)
print("Transpore of matrix is") 
print(m.transpose())