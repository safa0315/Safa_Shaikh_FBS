# 3. Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n

def sum_series(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total


n = int(input("Enter n: "))

result = sum_series(n)

print("Sum =", result)

#b
def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return fact


def sum_factorial(n):
    total = 0

    for i in range(1, n + 1):
        total = total + factorial(i)

    return total


n = int(input("Enter n: "))

result = sum_factorial(n)

print("Sum =", result)

#c
def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return fact


def sum_factorial(n):
    total = 0

    for i in range(1, n + 1):
        total = total + factorial(i)

    return total


n = int(input("Enter n: "))

result = sum_factorial(n)

print("Sum =", result)