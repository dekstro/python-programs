def sort_list(lst):
    lst.sort()
    return lst
lst=[int(i) for i in input("Enter number: ").split()]
res=sort_list(lst)
print(res)