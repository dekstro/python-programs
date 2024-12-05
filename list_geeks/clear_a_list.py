#Different ways to clear a list in Python
lst=[12,10,25,1,6,5]
#lst.clear() #1st  using clear method
#lst=[] #2nd reassign empty list
del(lst[:]) #3rd using del function
print(lst)