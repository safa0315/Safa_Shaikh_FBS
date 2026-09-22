#palindrome:

def check_digit(x):
    return True


def check_palindrome(num):
    digits = list(filter(check_digit, str(num)))

    reverse = digits[::-1]

    return digits == reverse


num = int(input("Enter a number: "))

print(check_palindrome(num))