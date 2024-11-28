lst=[10,20,-44,55,0,3]
n=int(input("Which no to find: "))
for i in lst:
    if n==i:
        print("Found")
        break
else:
    print("Not found")