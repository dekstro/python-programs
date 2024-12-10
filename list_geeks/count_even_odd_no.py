#Python program to count Even and Odd numbers in a List
lst = [2, 7, 5, 64, 14]
even_count=odd_count=0
for i in lst:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print('Even count',even_count,'\nOdd count',odd_count)