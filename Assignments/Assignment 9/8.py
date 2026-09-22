# Write a program to check whether a number is prime or not using recursion.

def prime(num, i):
    if i == num:
        return True

    if num % i == 0:
        return False

    return prime(num, i + 1)


num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
elif prime(num, 2):
    print("Prime number")
else:
    print("Not a prime number")