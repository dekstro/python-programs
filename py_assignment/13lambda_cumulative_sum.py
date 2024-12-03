import functools
lst=[5,9,-11,5,2,0,-2]
res=functools.reduce(lambda x,y: x+y,lst)
print(res)