#Create a lambda function to calculate cumulative product of all elements of a list.  
lst=[1,22,3,4]
import functools as ft
res=ft.reduce(lambda x,y: x*y, lst)
print(type(res))
print(res)