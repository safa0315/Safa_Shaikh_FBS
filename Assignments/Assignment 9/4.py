# Write a program to find sum of n numbers using recursion.

def sum_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_numbers(n - 1)


n = int(input("Enter n: "))

result = sum_numbers(n)

print("Sum =", result)