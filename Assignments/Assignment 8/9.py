# Write a program to check if entered number is a palindrome or
# not.


def reverse_number(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse


def check_palindrome(num):
    reverse = reverse_number(num)

    if num == reverse:
        return True
    else:
        return False


num = int(input("Enter a number: "))

if check_palindrome(num):
    print("Number is palindrome")
else:
    print("Number is not palindrome")