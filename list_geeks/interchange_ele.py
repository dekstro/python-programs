#Python program to interchange first and last elements in a list
lst = [1, 2, 3, 4, 5]
lst[0],lst[-1]=lst[-1],lst[0]
print(lst)