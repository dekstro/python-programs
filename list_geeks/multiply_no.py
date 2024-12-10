#Multiply All Numbers in the List in Python
import functools as ft
lst=[12,4,6,2,1]
res=ft.reduce(lambda x,y: x*y,lst)
print(res)

#another method
product=1
for i in lst:
    product=product*i
print(product)