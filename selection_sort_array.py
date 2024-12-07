from numpy import *
arr=array([3, 6, 1, 8, 2, 9])
n=len(arr)
for i in range(0,n):
    min=100
    mindx=-1
    for j in range(i,n):
        if arr[j]<min:
            min=arr[j]
            mindx=j
    temp=arr[i]
    arr[i]=arr[mindx]
    arr[mindx]=temp
print(arr)