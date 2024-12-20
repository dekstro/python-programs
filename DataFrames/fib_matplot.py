import matplotlib.pyplot as plt

# Function to generate Fibonacci numbers
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Generate the first 100 Fibonacci numbers
fib_numbers = fibonacci(100)

# Plotting the Fibonacci numbers
plt.figure(figsize=(10, 5))
plt.plot(fib_numbers, marker='o')
plt.title('First 100 Fibonacci Numbers')
plt.xlabel('Index')
plt.ylabel('Fibonacci Number')
plt.grid()
plt.show()