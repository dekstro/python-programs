numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Elements to remove
to_remove = [3, 5, 7]

for i in numbers:
    if i in to_remove:
        numbers.remove(i)
print(numbers)