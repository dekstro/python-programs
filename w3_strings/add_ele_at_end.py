'''Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'''
def ingly(s):
    if len(s)<3:
        return s
    if s[-3:]=='ing':
        return s+'ly'
    return s+'ing'
s=input('Enter string: ')
res=ingly(s)
print(res)