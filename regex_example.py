import re
str='man sun mop run cat rat mat get'
obj=re.search(r'm\w\w',str)
if obj:
    print(obj.group())
else:
    print('No match found')

#using findall
lst=re.findall(r'm\w\w',str)
print(lst)