# Write a program to print Fibonacci series using recursion.
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter number of terms: "))

for i in range(1, n + 1):
    print(fibonacci(i), end=" ")