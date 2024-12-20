'''Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'''
str1=input('Enter string: ')
char = str1[0]

# Replace all occurrences of the character 'char' with '$' in the 'str1' string.
str1 = str1.replace(char, '$')

# Reconstruct the 'str1' string by placing the original 'char' as the first character
# followed by the modified string starting from the second character.
str1 = char + str1[1:]
print(str1)

