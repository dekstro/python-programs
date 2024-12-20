'''Write a Python function that takes a list of words and return the longest word and the length of the longest one.
Sample Output:
Longest word: Exercises
Length of the longest word: 9'''
lst=['queen','termites','can','live','up','to','50','years']
maxx=0
for i in lst:
    maxx=max(maxx,len(i))
print(len('termites'))
print(maxx)