lst= [(1, 2), (), (3, 4), (), (5,)]
res = []

# Iterate over the list 'a'
for i in lst:
    
    if i: # If tuple is not empty then add it to res.
        res.append(i)

print(res)