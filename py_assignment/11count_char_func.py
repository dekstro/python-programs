# function to count no of character
def count_func(s):
    count=0
    for i in s:  # for loop will travel through the entire string
        count+=1  # here calc the no of character by adding 1 for each char
    return count
s=input("Enter a string: ")
res=count_func(s)
print("Number of character in %s is %d" %(s,res))