'''Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}'''
s='google.com'
dict={}
for i in s:
    keys=dict.keys()
    if i in keys:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)