str='vijay 20 1-5-2000, Rohit 21 22-07-2000'
import re
lst=re.findall(r'\d*-\d*-\d*',str)  #retrieve dob
print(lst)

#retrieve only ids
lst1=re.findall(r'\s\d+\s',str)
print(lst1)