lst=[10,20,'aaa','bbb',33.5,'ccc',88,'bbb',25]
count=0
for i in lst:
    if type(i)==str:
        count=count+1
print("The no of strings in list is",count)