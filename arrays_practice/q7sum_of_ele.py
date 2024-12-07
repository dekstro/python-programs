from numpy import *
arr=array([3, 6, 1, 8, 2, 9])

#7.Array CalculationsSum of Elements
#Write a program to calculate the sum of all elements in the array [1, 2, 3, 4, 5].
res=sum(arr)
print('Sum is',res)

#8.Largest and Smallest ElementWrite a program to find the largest and smallest numbers in the array [3, 6, 1, 8, 2, 9].
print('largest',max(arr))
print('smallest',min(arr))

#9.Average of Elements
#Write a program to calculate the average of the numbers in the array
avg=sum(arr)/len(arr)
print(avg)

#11.Count OccurrencesWrite a program to count the number of occurrences of the element 3 in the array [3, 1, 3, 3, 5, 6, 3].
count=0
for i in arr:
    if i==3:
        count+=1
print('Count is',count)

#12.Even and Odd Separation
#Write a program to separate even and odd numbers from the array [10, 15, 20, 25, 30].
even=[int(i) for i in arr if i%2==0]
odd=[int(i) for i in arr if i%2!=0]
print('Even elements:',even)
print('Odd elements:',odd)

#13.Second Largest ElementWrite a program to find the second largest number in the array [10, 20, 4, 45, 99].
arr.sort()
print('Second largest ele:',arr[len(arr)-2])

#14.Sort an Array
#Write a program to sort the array [6, 3, 8, 5, 2, 7, 4, 1] in ascending order.
sort_array=sort(arr)
print(sort_array)

#15.ChallengesRotate an Array
#Write a program to rotate the array [1, 2, 3, 4, 5] by two positions to the right. The result should be [4, 5, 1, 2, 3].
#case1 here we have to first reverse 0 to n-k-1 part ie., 1 2 3 after reverse 3 2 1
#2 then rverse n-k to n-1 part 4 5 after reverse 5 4
#3 then reverse entire array 0 to n-1 3 2 1 5 4 after reverse 4 5 1 2 3
#i will write a function to reverse and use this function to reverse for 3 cases
