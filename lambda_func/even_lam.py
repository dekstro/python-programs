#Write a lambda to test whether a given number is even or not.  
try:
    f=lambda x: 'Even' if x%2==0 and x!=0 else 'Not even'
    num=int(input('Enter a no: '))
    print(f(num))
except ValueError:
    print('Invalid input')
    print('Please enter input in Integer')
finally:
    print('Thank You')

