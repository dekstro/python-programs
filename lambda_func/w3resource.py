#Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.
'''
a=lambda x: x+15
b=lambda x,y: x*y
print(a(5))
print(b(2,3))
'''

#Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
#Sample Output:
#Power of the number of 15 = 
'''
f=lambda x,y: x**y
print(f(15,3)) #cube
'''

#Write a Python program to sort a list of tuples using Lambda.
#Original list of tuples:
#[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
#Sorting the List of Tuples:
#[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key=lambda x: x[1])
print("Sorting the List of Tuples:")
print(subject_marks) 
'''
