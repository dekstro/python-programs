import re
str='gopi 2222 vinay 9988 subha 89898 sri devi 124'
lst=re.findall(r'\D+',str)
print(lst)