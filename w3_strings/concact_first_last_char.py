'''Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String'''
s=input('Enter string: ')
str=''
n=len(s)
if n<2:
    print(str)
else:
    str=s[0:2]+s[n-2:n]
    print(str)