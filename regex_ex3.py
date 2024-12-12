#search for names starting with an or ak
import re
str='anil akhil anant arun arati arundhati abhijit ankur'
lst=re.findall(r'a[nk]\w*',str)
print(lst)