'''Array ManipulationsInsert an Element
Write a program to insert the number 50 at the third position of the array [10, 20, 30, 40, 60].'''
import numpy
arr=numpy.array([10, 20, 30, 40, 60])
arr=numpy.insert(arr,2,50)
print(arr)