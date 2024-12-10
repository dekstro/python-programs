#Sum of number digits in List
lst=[14,15,23,8,45]
res=[]
for ele in lst:
    sum=0
    for i in str(ele):
        sum=sum+int(i)
    res.append(sum)
print(res)