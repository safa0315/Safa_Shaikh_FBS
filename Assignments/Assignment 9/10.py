# 10. Write a program to reverse a number using recursion.

def reverse(num, rev):
    if num == 0:
        return rev

    digit = num % 10
    rev = rev * 10 + digit

    return reverse(num // 10, rev)


num = int(input("Enter a number: "))

result = reverse(num, 0)

print("Reverse =", result)